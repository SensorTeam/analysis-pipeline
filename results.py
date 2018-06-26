import math

# constants
# -----------------------------

DEVICE_d = 4.5e-3
DEVICE_r = 4e-2
# DEVICE_T = 0.0417
DEVICE_T = 0.5
DEVICE_P = 8e20
DEVICE_S = 1e12
DEVICE_q = 0.5
DEVICE_l = 550e-9
DEVICE_THETA_DEG = 30
MEDIUM_o = 0.9

# functions
# -----------------------------

def max_dist_intensity(A, k, T, P, r, S, q, o, theta_deg):
	theta = math.radians(theta_deg)

	a = math.tan(theta) ** 2
	b = 2 * r * math.tan(theta)
	c = (r ** 2) - ( (T * P * A * k * q * o) / (S * math.pi) )

	return ((-b) + math.sqrt( (b**2) - (4 * a * c) )) / (2 * a)

def max_dist_resolution(p, d, l):
	return (p * d) / (1.220 * l)

def min_shutter_speed(A, k, L, P, r, S, q, o, theta_deg):
	proj_area = math.pi * ( (r + (L * math.tan(math.radians(theta_deg)))) ** 2 )
	return (S * proj_area) / (P * A * k * q * o)

# species
# -----------------------------

targets = []

targets.append({
	'title': 'possum',
	'inter-pupil-distance': 4e-2,
	'pupil-diameter': 0.5e-2,
	'tl-efficiency': 1.0
})

targets.append({
	'title': 'fox',
	'inter-pupil-distance': 8e-2,
	'pupil-diameter': 0.25e-2,
	'tl-efficiency': 1.0
})

targets.append({
	'title': 'cow',
	'inter-pupil-distance': 12e-2,
	'pupil-diameter': 0.8e-2,
	'tl-efficiency': 1.0
})

# results
# -----------------------------

for target in targets:

	L_max_res = max_dist_resolution(
					target['inter-pupil-distance'],
					DEVICE_d,
					DEVICE_l
				)

	L_max_int = max_dist_intensity(
					math.pi * ((target['pupil-diameter']/2) ** 2),
					target['tl-efficiency'],
					DEVICE_T,
					DEVICE_P,
					DEVICE_r,
					DEVICE_S,
					DEVICE_q,
					MEDIUM_o,
					DEVICE_THETA_DEG
				)

	T_min = min_shutter_speed(
					math.pi * ((target['pupil-diameter']/2) ** 2),
					target['tl-efficiency'],
					L_max_res,
					DEVICE_P,
					DEVICE_r,
					DEVICE_S,
					DEVICE_q,
					MEDIUM_o,
					DEVICE_THETA_DEG
			)

	T_near = min_shutter_speed(
					math.pi * ((target['pupil-diameter']/2) ** 2),
					target['tl-efficiency'],
					10,
					DEVICE_P,
					DEVICE_r,
					DEVICE_S,
					DEVICE_q,
					MEDIUM_o,
					DEVICE_THETA_DEG
			)

	print target['title'].upper() + '\n---------------------'
	print 'MAX DIST for RESOLUTION: {:.2f} meters'.format(L_max_res)
	print 'MAX DIST for INTENSITY: {:.2f} meters'.format(L_max_int)
	print 'MIN SHUTTER SPEED at MAX DIST for RESOLUTION: {:.2f} seconds'.format(T_min)
	print 'MIN SHUTTER SPEED at 10 metres: {:.3f} seconds'.format(T_near)
	print '\n'