import cv2 as cv

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




if __name__ == '__main__':
	image = read('data/IMG_3361.JPG')
	image = downscale(image, 0.25)
	image = crop(image, 0.25)

	write(image, 'data/output.jpg')



