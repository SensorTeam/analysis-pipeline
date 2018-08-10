import cv2 as cv
import errno as er
from glob import glob

# Setup macros
# -----------------------------
MASKING_FACTOR = 0.7

# Functions
# -----------------------------
def read(file):
	return cv.imread(file)

def write(image, name):
	cv.imwrite(name, image)

def batch(path):
	# batch-reads image files and outputs a list of image dicts
	images = []
	files = glob(path)
	for file in files:
		try:
			images.append({
				'title': file[:-4],
				'image': read(file)
			})
		except IOError as e:
			if e.er != er.EISDIR:
				raise
	return images

def mask(image, factor):
	# applies binary thresholding
	gray_image = cv.cvtColor(image.copy(), cv.COLOR_BGR2GRAY)
	return cv.threshold(gray_image, int(255 * factor), 255, cv.THRESH_BINARY)[1]

def process(images):
	for image in images:
		masked = mask(image['image'], MASKING_FACTOR)
		write(masked, image['title'] + '_masked.jpg')
		print('Masked: {}'.format(image['title']))

# Main script
# -----------------------------
if __name__ == '__main__':
	try:
		images = batch('/data/*.jpg')
		process(images)

	except:
		print('Data not found. Reverting to demo test data...')
		demo = batch('/demo/mask/*.jpg')
		process(demo)


