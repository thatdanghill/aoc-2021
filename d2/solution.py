import numpy as n
p=print
s=sum
a=[l.split()for l in open('i.txt')]
a=[(c,int(v))for c,v in a]
f='forward'
d='down'
z=[(0,v)[c==f]for c,v in a]
x=s(z)
m=[((-v,v)[c==d],0)[c==f]for c,v in a]
y=s(m)
p(x*y)
y=s(n.cumsum(m)*z)
p(x*y)