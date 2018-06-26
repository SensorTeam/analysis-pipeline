import re
import cv2 as cv
import errno as er
import colorsys as cs
from glob import glob

# Setup matplotlib for virtualenv
# --------------------------------
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as pl

from matplotlib import rc

rc('font',**{'family':'serif','serif':['Times New Roman']})

# Setup macros
# --------------------------------
EXPOSURE_TIMES_LABELS = [
	'2',
	'1.6',
	'1.3',
	'1',
	'0.8',
	'0.6',
	'0.5',
	'0.4',
	'0.3',
	'1/4',
	'1/5',
	'1/6',
	'1/8',
	'1/10',
	'1/13',
	'1/15',
	'1/20',
	'1/25',
	'1/30',
	'1/40',
	'1/50',
	'1/60',
]

DISTANCE_LABELS = [
	str(x) for x in range(10, 110, 10)
]

# Functions
# --------------------------------
def read(file):
	return cv.imread(file)

def batch(path):
	# batch-reads image files and outputs a list of image dicts
	images = []
	files = glob(path)
	for file in files:
		try:
			images.append({
				'title': file,
				'score': None,
				'image': read(file),
				'order': int(re.search(r'\d+',file).group()) # assumes each file is numbered, so an order can be assigned to it
			})
		except IOError as e:
			if e.er != er.EISDIR:
				raise
	return images

def get_intensity(image):
	# looks at all pixels of a photo and outputs an intensity score
	width = image.shape[1]
	height = image.shape[0]
	intensity = 0
	for row in range(0, height):
		row_intensity = 0
		for pixel in range(0, width):
			rgb = image[row][pixel]
			hsv = cs.rgb_to_hsv(
					rgb[0] / 255,
					rgb[1] / 255,
					rgb[2] / 255
				)
			# intensity equals saturation * value of a pixel
			row_intensity += hsv[1] * hsv[2]
		intensity += row_intensity
	return intensity

def sort(images):
	return sorted(images, key=lambda image: image['order'])

def get_intesities(images):
	# given a list of images (a collection of dicts), find their intensities and return a list of intensities
	intensities = []
	for image in images:
		image['score'] = get_intensity(image['image'])
		intensities.append(
			image['score']
		)
		print('{}: {:.2f}'.format(image['title'], image['score']))
	return intensities

def normalise(intensities):
	# converts intensitities to a linear value from 0 to 1
	highest_intensity = intensities[0]
	for intensity in intensities:
		if intensity > highest_intensity:
			highest_intensity = intensity

	normalised_intensities = []
	for intensity in intensities:
		normalised_intensities.append(
			intensity / highest_intensity
		)
	return normalised_intensities

def process(title, path):
	# batch processes a folder
	images = batch(path)
	images = sort(images)
	intensities = get_intesities(images)
	intensities = normalise(intensities)
	return intensities

# Main functionality
# --------------------------------
if __name__ == '__main__':

	pl.figure(figsize=(8, 3))
	ax = pl.subplot(111)

	try:
		possum = process('Possum', 'data/IvT/Original/Possum/*.jpg')
		fox = process('Fox', 'data/IvT/Original/Fox/*.jpg')
		cow = process('Cow', 'data/IvT/Original/Cow/*.jpg')

		possum = list(reversed(possum))
		fox = list(reversed(fox))
		cow = list(reversed(cow))

		EXPOSURE_TIMES_LABELS = list(reversed(EXPOSURE_TIMES_LABELS))


		ax.plot(EXPOSURE_TIMES_LABELS, possum, 'ko', label='Possum (5.0 mm)')
		ax.plot(EXPOSURE_TIMES_LABELS, fox, 'ks', label='Fox (2.5 mm)')
		ax.plot(EXPOSURE_TIMES_LABELS, cow, 'kD', label='Cow (8.0 mm)')

		pl.xlabel('Exposure time(s)')
		pl.ylabel('Total saturation (%)')

	except:
		# print('Data not found. Reverting to demo test data...')
		# demo = process('Test', 'test/*.png')
		# pl.plot(['01', '02', '03', '04', '05'], demo, 'kx', label='Test Data')

		control = process('Test', 'control/*.png')
		pl.plot(['A', 'B', 'C', 'D', 'E', 'F'], control, 'ko', label='Test Data')

		pl.ylabel('Total saturation (%)')
		pl.xlabel('Images')

	ax.spines['right'].set_visible(False)
	ax.spines['top'].set_visible(False)

	leg = pl.legend(frameon=False)

	pl.savefig('main.svg', bbox_inches='tight')

