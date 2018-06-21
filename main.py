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

def mask(image):
	gray_image = cv.cvtColor(image.copy(), cv.COLOR_BGR2GRAY)
	return cv.threshold(gray_image, 200, 255, cv.THRESH_BINARY)[1]

def batch():
	files = glob('data/*.JPG')
	for file in files:
		try:
			image = read(file)
			image = downscale(image, 0.25)
			image = crop(image, 0.25)
			write(image, file[:-4] + '_cropped.jpg')
			image = mask(image)
			write(image, file[:-4] + '_masked.jpg')

		except IOError as e:
			if e.errno != eerno.EISDIR:
				raise

def intensity(image):
	# assumes image is cropped to spectra

	width = image.shape[1]
	height = image.shape[0]
	gray_image = cv.cvtColor(image.copy(), cv.COLOR_BGR2GRAY)

	for i in range(0, height):
		# for each row
		# get row average intensity and add it to total
		for j in range(0, width):
			# for each pixel
			# get pixel 'score' between 0 to 255 and divide total 'score' by width
			# add it to to the average row intensity

	# divide total score by height to get intensity

if __name__ == '__main__':
	batch()



