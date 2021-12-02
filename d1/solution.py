import sys,numpy as n
a=n.array([int(l)for l in open(sys.argv[1])])
b=n.convolve(a,n.ones(3),'valid')
print(f'silver: {((a[1:]-a[:-1])>0).sum()}\ngold: {((b[1:]-b[:-1])>0).sum()}')

