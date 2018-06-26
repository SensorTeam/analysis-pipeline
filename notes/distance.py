import math

def max_dist(p,d,l):
	return (p * d) / (1.22 * l)

def max_dist_alt(p,d,l):
	return p / ( math.asin(1.22 * (l/d)) )

def aperture(f,F):
	return f/F

f = 18e-3
F = 4.0

p = 4e-2
d = aperture(f,F)

l = 580e-9

L = max_dist(p,d,l)
L_alt = max_dist_alt(p,d,l)

L_human = max_dist(1e-3, 4e-3, l)

print '{:.2f} metres'.format(L)
print '{:.2f} metres (alt)'.format(L_alt)

print '----'

print 'HUMAN: {:.2f} metres'.format(L_human)
