import math

def projected_area(spotlight_radius, distance, spotlight_spread):
	theta = math.radians(spotlight_spread)
	delta_radius = distance * math.tan(theta)
	projected_radius = spotlight_radius + delta_radius
	return math.pi * (projected_radius)

def percent_reflected(pupil_area, projected_area):
	return pupil_area / projected_area

spotlight_radius = 4e-2
distance = 100
spotlight_spread = 45

qe = 0.5
R = 0.5

photons = 10e20

pupil_area = math.pi * (1e-2 ** 2)

percent = percent_reflected(pupil_area, projected_area(spotlight_radius, distance, spotlight_spread))

result = photons * percent * qe * R

print '{} photons are reflected in one second'.format(result)

min_photons = 40e4

if result > min_photons:
	print 'detected'
else:
	print 'not visible'

