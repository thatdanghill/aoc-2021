import sys
r=range(12)
a=[[2**(11-i)*int(l[i])for l in open(sys.argv[1])]for i in r]
v=lambda x,c,b:[x(sorted(i)[::c],key=i.count)for i in b]
y=max,-1
z=min,1
def f(x):
    *l,=zip(*a)
    for i in r:
        n=v(*x,zip(*l))[i]
        l=[j for j in l if n==j[i]]
        if len(l) == 1:
            return sum(l[0])
print(f'Silver: {sum(v(*y,a))*sum(v(*z,a))}\nGold: {f(y)*f(z)}')
