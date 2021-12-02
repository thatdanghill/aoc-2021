import numpy as n
p=print
f=open('i.txt')
a=[l.split()for l in f.readlines()]
a=[(l[0], int(l[1]))for l in a]
f='forward'
d='down'
x=sum([(0,v)[c==f]for c,v in a])
m=[((-v,v)[c==d],0)[c==f]for c,v in a]
y=sum(m)
p(x*y)
y=sum(n.cumsum(m)*[(0,v)[c==f]for c,v in a])
p(x*y)