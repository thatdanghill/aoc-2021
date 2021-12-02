import numpy as n
p=print
f=open('i.txt')
a=n.array([int(l)for l in f.readlines()])
p(((a[1:]-a[:-1]) > 0).sum())
b=n.convolve(a,n.ones(3),'valid')
p(((b[1:]-b[:-1]) > 0).sum())

