import sys
r=range(12)
s=sum
a=[[2**(11-i)*int(l[i])for i in r]for l in open(sys.argv[1])]
v=lambda x,c,b:[x(sorted(i)[::c],key=i.count)for i in zip(*b)]
y=max,-1
z=min,1
def f(x,l=a):
 for i in r:
  l=[j for j in l if v(*x,l)[i]==j[i]]
  if len(l)<2:return s(l[0])
print(f'Silver: {s(v(*y,a))*s(v(*z,a))}\nGold: {f(y)*f(z)}')