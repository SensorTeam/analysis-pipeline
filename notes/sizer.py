import math

def sol_S(T, P, A, r, L, theta_deg):
	theta = math.radians(theta_deg)

	delta_r = L * math.tan(theta)
	proj_r = r + delta_r

	proj_A = math.pi * (proj_r ** 2)

	return (T * P * A) / proj_A

# -------------------------------------

T = 1
P = 1e20
A = math.pi * (1e-2 ** 2)
r = 4e-2
L = 100
theta_deg = 10

S = sol_S(T, P, A, r, L, theta_deg)

print S

# -------------------------------------

def sol_L(T, P, A, r, S, theta_deg):
	theta = math.radians(theta_deg)

	a = math.tan(theta) ** 2
	b = 2 * r * math.tan(theta)
	c = (r ** 2) - ( (T * P * A) / (S * math.pi) )

	return ((-b) + math.sqrt( (b**2) - (4 * a * c) )) / (2 * a)

# -------------------------------------

new_L = sol_L(T, P, A, r, S, theta_deg)

print new_L
