import math

# FORMULAE
# ---------------

def percentage_intensity(R, A, r, L, theta_deg):
	theta_rad = math.radians(theta_deg)
	delta_r = L * math.tan(theta_rad)
	projected_r = r + delta_r
	projected_area = math.pi * (projected_r ** 2)

	return (R * A) / projected_area

# VARS
# ---------------

spread = 0
intensity = 500
spotlight_radius = 10

opacity = 1.0
distance = 10

pupil_area = math.pi * (1 ** 2)

p = percentage_intensity(opacity, pupil_area, spotlight_radius, distance, spread)

print(p)