import numpy as n
p=print
f=open('i.txt')
a=[l.split()for l in f.readlines()]
a=[(l[0], int(l[1]))for l in a]
f='forward'
d='down'
z=[(0,v)[c==f]for c,v in a]
x=sum(z)
m=[((-v,v)[c==d],0)[c==f]for c,v in a]
y=sum(m)
p(x*y)
y=sum(n.cumsum(m)*z)
p(x*y)