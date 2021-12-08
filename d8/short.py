import sys
A=[(i.split(),j.split())for i,j in[i.split('|')for i in open(sys.argv[1])]]
v=lambda i:''.join(sorted(i))
O=0
L=len
r={2:1,3:7,4:4,7:8}
for S,D in A:
 M={}
 for s in S:M[r.get(L(s))]=v(s)
 m={*M[1]}
 for s in S:
  s,Y,Z=v(s),~L({*M[4]}-m-{*s})+2,~L(m-{*s})+2
  M[((10,((0,9)[Y],6)[~Z+2])[L(s)==6],((2,5)[Y],3)[Z])[L(s)==5]]=s
 O+=int(''.join([str({i:j for j,i in M.items()if j!=10}[v(k)])for k in D]))
print(f'Silver: {sum([L(j)in[2,3,4,7]for _,i in A for j in i])}\nGold: {O}')