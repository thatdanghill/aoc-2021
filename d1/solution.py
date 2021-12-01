import numpy as np

with open('input.txt', 'r') as f:
    a = np.array([int(l) for l in f.readlines()])
print(((a[1:]-a[:-1]) > 0).sum())
b=np.convolve(a,np.ones(3),'valid')
print(((b[1:]-b[:-1]) > 0).sum())

