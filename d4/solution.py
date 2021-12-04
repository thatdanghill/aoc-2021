import sys
O,*R=open(sys.argv[1])
O=[int(i)for i in O.split(',')]
l,r,*K=len,range
s=sum
v=lambda x:[x[i:i+5]for i in r(0,l(x),5)]
c=lambda x,y:s([s([i*(~j+2)for i,j in zip(m,n)])for m,n in zip(x,y)])
u=lambda x:5in[s(i)for i in x]
A=v(v([int(i) for j in R for i in j.split()]))
L=25*l(A)
B=v(v([0]*L))
for i in r(l(O)*L):
 j,k,m,n=i//L,(i//25)%(l(A)),(i//5)%5,i%5
 J,H=O[j],A[k]
 if H[m][n]==J:B[k][m][n]=1
 if (m==n>3)*(u(B[k])or u(zip(*B[k])))*(k not in K):K+=[k,J*c(H,B[k])]
print(f'Silver: {K[1]}\nGold: {K[-1]}')