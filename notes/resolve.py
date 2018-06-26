def max_dist(p,d,l):
	return (p * d) / (1.22 * l)

def aperture(f,F):
	return f/F

f = 18e-3
F = 4.0

p_min = 4e-3
p_mid = 6e-3
p_max = 8e-3

d_human = 3e-3
d_dslr = aperture(f,F)
d_phone = 1.8e-3

l = 550e-9

print 'HUMAN MIN: {:.2f} metres'.format(max_dist(p_min, d_human, l))
print 'HUMAN MID: {:.2f} metres'.format(max_dist(p_mid, d_human, l))
print 'HUMAN MAX: {:.2f} metres'.format(max_dist(p_max, d_human, l))

print '----'

print 'DSLR MIN: {:.2f} metres'.format(max_dist(p_min, d_dslr, l))
print 'DSLR MID: {:.2f} metres'.format(max_dist(p_mid, d_dslr, l))
print 'DSLR MAX: {:.2f} metres'.format(max_dist(p_max, d_dslr, l))

print '----'

print 'PHONE MIN: {:.2f} metres'.format(max_dist(p_min, d_phone, l))
print 'PHONE MID: {:.2f} metres'.format(max_dist(p_mid, d_phone, l))
print 'PHONE MAX: {:.2f} metres'.format(max_dist(p_max, d_phone, l))


