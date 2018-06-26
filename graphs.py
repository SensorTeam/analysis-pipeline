import math

# Setup matplotlib for virtualenv
# --------------------------------
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as pl

from matplotlib import rc
rc('font',**{'family':'serif','serif':['Times New Roman']})

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

DISTANCE_LABELS = [
	str(x) for x in range(10, 110, 10)
]

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

exposures = []

for target in targets:

	T_s = []

	for L in range(10, 110, 10):

		T = min_shutter_speed(
						math.pi * ((target['pupil-diameter']/2) ** 2),
						target['tl-efficiency'],
						L,
						DEVICE_P,
						DEVICE_r,
						DEVICE_S,
						DEVICE_q,
						MEDIUM_o,
						DEVICE_THETA_DEG
				)

		T_s.append(T)

	exposures.append(T_s)

pl.figure(figsize=(8, 3))

ax = pl.subplot(111)

ax.plot(DISTANCE_LABELS, exposures[0], 'ko', label='Possum')
ax.plot(DISTANCE_LABELS, exposures[1], 'ks', label='Fox')
ax.plot(DISTANCE_LABELS, exposures[2], 'kD', label='Cow')

pl.xlabel('Distance (m)')
pl.ylabel('Exposure time (s)')

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

leg = pl.legend(frameon=False)

pl.savefig('graph.svg', bbox_inches='tight')
# pl.show()