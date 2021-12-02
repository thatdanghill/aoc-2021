import sys,numpy as n
s=sum
a=[(l.split()[0][0],int(l.split()[1]))for l in open(sys.argv[1])]
z=[v*(c=='f')for c,v in a]
m=[(-v,v)[c<'e']*(c!='f')for c,v in a]
print(f'silver: {s(z)*s(m)}\ngold: {s(z)*s(n.cumsum(m)*z)}')