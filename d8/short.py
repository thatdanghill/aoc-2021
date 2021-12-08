import sys
A=[i.split('|')for i in open(sys.argv[1])]
v=lambda i:''.join(sorted(i))
O=P=0
L=len
r={2:1,3:7,4:4,7:8}
for S,D in A:
 S,D=S.split(),D.split()
 M={}
 for s in S:M[r.get(L(s))]=v(s)
 for i in D:P+=L(i)in r
 m={*M[1]}
 for s in S:
  s,Y,Z=v(s),~L({*M[4]}-m-{*s})+2,~L(m-{*s})+2
  M[((10,((0,9)[Y],6)[~Z+2])[L(s)==6],((2,5)[Y],3)[Z])[L(s)==5]]=s
 O+=int(''.join([str({i:j for j,i in M.items()if j!=10}[v(k)])for k in D]))
print(f'Silver: {P}\nGold: {O}')