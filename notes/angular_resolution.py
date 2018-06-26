import math

def angle_in_rad(l, D):
	return l / D

def max_dist(p, theta):
	return p / (2 * math.tan(theta/2))

D = 1.8e-3
l = 580e-9
p = 12e-2

L = max_dist(p, angle_in_rad(l, D))

print '{} metres'.format(L)



