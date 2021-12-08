import sys
A=[(i.split(),j.split())for i,j in[i.split('|')for i in open(sys.argv[1])]]
v=lambda i:''.join(sorted(i))
O=0
L=len
r={2:1,3:7,4:4,7:8}
for S,D in A:
    M={}
    for s in S:M[r.get(L(s))]=v(s)
    c,f=M[1]
    b,d={*M[4]}-{c,f}
    for s in S:
        s,Y,Z=v(s),(b in s)*(d in s),(c in s)*(f in s)
        M[((10,((0,9)[Y],6)[~Z+2])[L(s)==6],((2,5)[Y],3)[Z])[L(s)==5]]=s
    O+=int(''.join([str({i:j for j,i in M.items() if j!=10}[v(k)])for k in D]))
print(f'Silver: {sum([L(j)in[2,3,4,7]for _,i in A for j in i])}\nGold: {O}')