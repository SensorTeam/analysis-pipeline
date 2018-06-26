import errno
import cv2 as cv
from glob import glob

def downscale(image, factor):
	scaled_width = int(image.shape[1] * factor)
	scaled_height = int(image.shape[0] * factor)
	scaled_dimensions = (scaled_width, scaled_height)
	return cv.resize(image, scaled_dimensions, interpolation = cv.INTER_AREA)

def read(file):
	return cv.imread(file)

def write(image, file):
	cv.imwrite(file, image)

def crop(image, factor):
	width = image.shape[1]
	height = image.shape[0]
	trim = (1 - factor) / 2
	crop_start = int(width * trim)
	crop_end = int(width * (trim + factor))
	return image[0:height, crop_start:crop_end]

def trim(image, factor):
	width = image.shape[1]
	trimmed_height = int(image.shape[0] * factor)
	return image[0:trimmed_height, 0:width]

def mask(image, factor):
	gray_image = cv.cvtColor(image.copy(), cv.COLOR_BGR2GRAY)
	return cv.threshold(gray_image, int(255 * factor), 255, cv.THRESH_BINARY)[1]

def intensity(image):
	width = image.shape[1]
	height = image.shape[0]
	gray_image = cv.cvtColor(image.copy(), cv.COLOR_BGR2GRAY)

	score = 0

	for row in range(0, height):
		row_score = 0
		for pixel in range(0, width):
			row_score += gray_image[row][pixel]
		score += row_score

	return score

def batch():
	files = glob('data/*.jpg')
	for file in files:
		try:
			image = read(file)
			# image = downscale(image, 0.25)
			# image = crop(image, 0.1)
			# image = trim(image, 0.6)
			# write(image, file[:-4] + '_cropped.jpg')

			# image = mask(image, 0.7) # 10-50m
			image = mask(image, 0.4) # 60-100m
			
			write(image, file[:-4] + '_masked.jpg')

		except IOError as e:
			if e.errno != eerno.EISDIR:
				raise

def batch_new():
	files = glob('data/*.jpg')
	for file in files:
		try:
			image = read(file)
			print(file)
			print(intensity(image))


		except IOError as e:
			if e.errno != eerno.EISDIR:
				raise

if __name__ == '__main__':
	batch()



