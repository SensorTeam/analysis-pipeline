def max_dist(p, d, l):
	return (p * d) / (1.22 * l)

# species
# -------------

p_possum = 4e-2
p_fox = 6e-2
p_cow = 12e-2

# device
# -------------

l = 550e-9
d_human = 5e-3
d_phone = 1.8e-3
d_dslr = 18e-3 / 4.0

# results
# -------------

print '\nPOSSUM'
print '------------'
print 'HUMAN: {:.2f} metres'.format(max_dist(p_possum, d_human, l))
print 'PHONE: {:.2f} metres'.format(max_dist(p_possum, d_phone, l))
print 'DSLR: {:.2f} metres'.format(max_dist(p_possum, d_dslr, l))

print '\nFOX'
print '------------'
print 'HUMAN: {:.2f} metres'.format(max_dist(p_fox, d_human, l))
print 'PHONE: {:.2f} metres'.format(max_dist(p_fox, d_phone, l))
print 'DSLR: {:.2f} metres'.format(max_dist(p_fox, d_dslr, l))

print '\nCOW'
print '------------'
print 'HUMAN: {:.2f} metres'.format(max_dist(p_cow, d_human, l))
print 'PHONE: {:.2f} metres'.format(max_dist(p_cow, d_phone, l))
print 'DSLR: {:.2f} metres'.format(max_dist(p_cow, d_dslr, l))

