import math

def projected_area(spotlight_radius, distance, spotlight_spread):
	theta = math.radians(spotlight_spread)
	delta_radius = distance * math.tan(theta)
	projected_radius = spotlight_radius + delta_radius
	return math.pi * (projected_radius)

def percent_reflected(pupil_area, projected_area):
	return pupil_area / projected_area

spotlight_radius = 4e-2
distance = 50
spotlight_spread = 10

watts = 10

pupil_area = math.pi * (1e-2 ** 2)

percent = percent_reflected(pupil_area, projected_area(spotlight_radius, distance, spotlight_spread))

result = watts * percent

print '{} watts are reflected'.format(result)

