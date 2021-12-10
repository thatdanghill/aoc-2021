import sys
O={'{':'}','[':']','(':')','<':'>'}
P={')':3,']':57,'}':1197,'>':25137}
Q={')':1,']':2,'}':3,'>':4}
S=0
G=[]
for A in open(sys.argv[1]):
 C=[]
 t=g=0
 for c in A[:-1]:
  if c in O:C=[O[c]]+C
  elif c!=C.pop(0):
   S+=P[c]
   t=1
   break
 if ~t+2:
  for c in C:g=g*5+Q[c]
  G+=[g]
print(f'Silver: {S}\nGold: {sorted(G)[len(G)//2]}')