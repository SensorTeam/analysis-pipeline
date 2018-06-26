def max_dist(p,d,l):
	return (p * d) / (1.22 * l)

p = 8e-2
d = 18e-3 / 4.0
l = 550e-9

print '{:.2f} metres'.format(max_dist(p,d,l))