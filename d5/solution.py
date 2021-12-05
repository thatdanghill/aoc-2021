import sys
A=[[int(i)for i in l.replace('->',',').split(',')]for l in open(sys.argv[1])]
G=lambda x:x and 1|-(x<0)
def f(C):
 b=[[0]*1000for _ in[0]*1000]
 for X,Y,W,Z in C:
  T,U=W-X,Z-Y
  for x,y in[(X+i*G(T),Y+i*G(U))for i in range(max(abs(U),abs(T))+1)]:b[y][x]+=1
 return sum([1for i in b for j in i if j>1])
print(f'Silver: {f([l for l in A if(l[0]==l[2])|(l[1]==l[3])])}\nGold: {f(A)}')