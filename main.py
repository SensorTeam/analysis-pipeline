import cv2 as cv

def downscale(image, factor):
	scaled_width = int(image.shape[1] * factor)
	scaled_height = int(image.shape[0] * factor)
	scaled_dimensions = (scaled_width, scaled_height)
	return cv.resize(image, scaled_dimensions, interpolation = cv.INTER_AREA)

def read(file):
	return cv.imread(file)

def write(image):
	cv.imwrite('data/output.jpg', image)

if __name__ == '__main__':
	image = read('data/IMG_3361.JPG')
	image = downscale(image, 0.25)

	write(image)



