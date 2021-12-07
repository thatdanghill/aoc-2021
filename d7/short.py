import sys
F,=open(sys.argv[1])
A=sorted([int(i)for i in F.split(',')])
L=len(A)
g=sum(A)//L
v=lambda x:sum([(j:=abs(i-x))*(j+1)/2for i in A])
print(f'Silver: {sum([abs(i-A[L//2])for i in A])}\nGold: {min(v(g),v(g+1))}')