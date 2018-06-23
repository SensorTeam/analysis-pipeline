import cv2 as cv
import colorsys as cs

import errno
from glob import glob

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

TIMES = [
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

DISTANCES = [x for x in range(10, 110, 10)]

def intensity(image):
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
			row_intensity += hsv[1] * hsv[2]
		intensity += row_intensity
	return intensity

def read(file):
	return cv.imread(file)

def batch(path):
	images = []
	files = glob(path)
	for file in files:
		try:
			images.append({
				'title': file,
				# 'number': int(file[-6:-4]),
				'number': int(file[-8:-5]),
				'data': read(file),
				'intensity': None
			})
		except IOError as e:
			if e.errno != errno.EISDIR:
				raise
	return images

def find_max(intensities):
	best = intensities[0]
	for intensity in intensities:
		if intensity > best:
			best = intensity
	return best

def normalise(intensities):
	normalised_intensities = []
	highest = find_max(intensities)
	for intensity in intensities:
		normalised_intensities.append(
				intensity/highest
			)
	return normalised_intensities

if __name__ == '__main__':
	# print('Cow')
	# cow_images = batch('data/IvT/Original/Cow/*.jpg')
	# cow_images = sorted(cow_images, key=lambda image: image['number'])

	# cow_numbers = []
	# cow_intensities = []

	# for image in cow_images:
	# 	image['intensity'] = intensity(image['data'])
	# 	print('{}: {:.2f}'.format(image['number'], image['intensity']))
	# 	cow_numbers.append(image['number'])
	# 	cow_intensities.append(image['intensity'])

	# print('Fox')
	# fox_images = batch('data/IvT/Original/Fox/*.jpg')
	# fox_images = sorted(fox_images, key=lambda image: image['number'])

	# fox_numbers = []
	# fox_intensities = []

	# for image in fox_images:
	# 	image['intensity'] = intensity(image['data'])
	# 	print('{}: {:.2f}'.format(image['number'], image['intensity']))
	# 	fox_numbers.append(image['number'])
	# 	fox_intensities.append(image['intensity'])

	# print('Possum')
	# possum_images = batch('data/IvT/Original/Possum/*.jpg')
	# possum_images = sorted(possum_images, key=lambda image: image['number'])

	# possum_numbers = []
	# possum_intensities = []

	# for image in possum_images:
	# 	image['intensity'] = intensity(image['data'])
	# 	print('{}: {:.2f}'.format(image['number'], image['intensity']))
	# 	possum_numbers.append(image['number'])
	# 	possum_intensities.append(image['intensity'])

	# cow_intensities = normalise(cow_intensities)
	# fox_intensities = normalise(fox_intensities)
	# possum_intensities = normalise(possum_intensities)

	# plt.plot(TIMES, cow_intensities, 'kx', label='Cow (8.0 mm)')
	# plt.plot(TIMES, fox_intensities, 'k+', label='Fox (2.5 mm)')
	# plt.plot(TIMES, possum_intensities, 'k*', label='Possum (5.0 mm)')
	# plt.xlabel('Exposure time (s)')
	# plt.ylabel('Spectrum saturation (%)')
	# # plt.ylabel('Saturation score')
	# plt.legend()
	# plt.show()


	print('Cow')
	cow_images = batch('data/IvD/Original/Cow/*.jpg')
	cow_images = sorted(cow_images, key=lambda image: image['number'])

	cow_intensities = []

	for image in cow_images:
		image['intensity'] = intensity(image['data'])
		print('{}: {:.2f}'.format(image['number'], image['intensity']))
		cow_intensities.append(image['intensity'])

	cow_intensities = normalise(cow_intensities)

	plt.plot(DISTANCES, cow_intensities, 'kx', label='Cow (8.0 mm)')
	plt.xlabel('Exposure time (s)')
	plt.ylabel('Spectrum saturation (%)')
	# plt.ylabel('Saturation score')
	plt.legend()
	plt.show()

		
