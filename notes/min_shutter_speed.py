import math

def min_shutter_speed(L, P, A, r, S, theta_deg, k, q, o):
	proj_area = math.pi * ( (r + (L * math.tan(math.radians(theta_deg)))) ** 2 )
	return (S * proj_area) / (P * A * k * q * o)

# L: distance
L = 30
# P: photons emitted by spotlight
P = 1e20
# A: pupil area of target
A = math.pi * (1e-2 ** 2)
# r: radius of spotlight exit surface
r = 4e-2
# S: photons required to create a white pixel
S = 1e12
# theta_deg: beam divergence
theta_deg = 30
# k: TL reflection efficiency
k = 0.9
# q: quantum efficiency of sensor
q = 0.5
# o: opacity of medium
o = 0.9

T_min = min_shutter_speed(L, P, A, r, S, theta_deg, k, q, o)

print '{:.2f} seconds'.format(T_min)