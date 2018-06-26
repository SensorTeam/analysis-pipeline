import math

def fov(L,angle):
	theta = math.radians(angle)
	return 2 * L * math.tan(theta)

def ang(dimension, f):
	return 2 * math.atan(dimension / (2 * f))

L = 107.30
angle = ang()

print '{:.2f} metres'.format(fov(L, angle))