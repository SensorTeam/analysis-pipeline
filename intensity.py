import cv2 as cv
import colorsys as cs

import errno
from glob import glob

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

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
				'number': int(file[-6:-4]),
				'data': read(file),
				'intensity': None
			})
		except IOError as e:
			if e.errno != errno.EISDIR:
				raise
	return images

if __name__ == '__main__':
	print('Cow')
	cow_images = batch('data/IvT/Original/Cow/*.jpg')
	cow_images = sorted(cow_images, key=lambda image: image['number'])

	cow_numbers = []
	cow_intensities = []

	for image in cow_images:
		image['intensity'] = intensity(image['data'])
		print('{}: {:.2f}'.format(image['number'], image['intensity']))
		cow_numbers.append(image['number'])
		cow_intensities.append(image['intensity'])

	print('Fox')
	fox_images = batch('data/IvT/Original/Fox/*.jpg')
	fox_images = sorted(fox_images, key=lambda image: image['number'])

	fox_numbers = []
	fox_intensities = []

	for image in fox_images:
		image['intensity'] = intensity(image['data'])
		print('{}: {:.2f}'.format(image['number'], image['intensity']))
		fox_numbers.append(image['number'])
		fox_intensities.append(image['intensity'])

	print('Possum')
	possum_images = batch('data/IvT/Original/Possum/*.jpg')
	possum_images = sorted(possum_images, key=lambda image: image['number'])

	possum_numbers = []
	possum_intensities = []

	for image in possum_images:
		image['intensity'] = intensity(image['data'])
		print('{}: {:.2f}'.format(image['number'], image['intensity']))
		possum_numbers.append(image['number'])
		possum_intensities.append(image['intensity'])

	plt.plot(cow_numbers, cow_intensities, 'ko')
	plt.plot(fox_numbers, fox_intensities, 'kx')
	plt.plot(possum_numbers, possum_intensities, 'k+')

	plt.show()
		
