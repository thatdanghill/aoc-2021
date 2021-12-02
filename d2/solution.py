import numpy as n
p=print
s=sum
a=[l.split()for l in open('i')]
a=[(c,int(v))for c,v in a]
f='forward'
d='down'
z=[(0,v)[c==f]for c,v in a]
m=[((-v,v)[c==d],0)[c==f]for c,v in a]
p(s(z)*s(m))
p(s(z)*s(n.cumsum(m)*z))