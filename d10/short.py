import sys
O,P,*G='([{<',')]}>'
Q=[3,57,1197,25137]
S=0
for A in open(sys.argv[1]):
 t,g,*C=0,0
 for c in A[:-1]:
  if c in O:C=[P[O.index(c)]]+C
  elif c!=C.pop(0):S,t=S+Q[P.index(c)],1
 if~t+2:
  for c in C:g=g*5+P.index(c)+1
  G+=[g]
print(f'Silver: {S}\nGold: {sorted(G)[len(G)//2]}')