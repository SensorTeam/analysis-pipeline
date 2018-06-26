def max_dist_resolution(p, d, l):
	return (p * d) / (1.220 * l)

# p: inter-pupillary distance
p = 12e-2
# d: aperture diameter
d = 18e-3/4.0
# l: wavelength
l = 550e-9

L_max = max_dist_resolution(p, d, l)

print '{:.2f} metres'.format(L_max)