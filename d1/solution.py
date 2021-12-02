import numpy as n
p=print
a=n.array([int(l)for l in open('i.txt')])
p(((a[1:]-a[:-1]) > 0).sum())
b=n.convolve(a,n.ones(3),'valid')
p(((b[1:]-b[:-1]) > 0).sum())

