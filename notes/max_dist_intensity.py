import math

def max_dist_intensity(T, P, A, r, S, theta_deg, k, q, o):
	theta = math.radians(theta_deg)

	a = math.tan(theta) ** 2
	b = 2 * r * math.tan(theta)
	c = (r ** 2) - ( (T * P * A * k * q * o) / (S * math.pi) )

	return ((-b) + math.sqrt( (b**2) - (4 * a * c) )) / (2 * a)

# T: shutter speed
T = 0.5
# P: photons emitted by spotlight
P = 1e20
# A: pupil area of target
A = math.pi * (0.4e-2 ** 2)
# r: radius of spotlight exit surface
r = 4e-2
# S: photons required to create a white pixel
S = 2e11
# theta_deg: beam divergence
theta_deg = 30
# k: TL reflection efficiency
k = 0.9
# q: quantum efficiency of sensor
q = 0.5
# o: opacity of medium
o = 0.9

L_max = max_dist_intensity(T, P, A, r, S, theta_deg, k, q, o)

print '{:.2f} metres'.format(L_max)