import sys
F,=open(sys.argv[1])
A=[int(i)for i in F.split(',')]
def f(g):
 O,N=[A.count(i)for i in range(7)],[0]*9
 for _ in[1]*g:
  O=O[1:]+[O[0]+N[0]]
  N=N[1:]+[O[6]]
 return sum(O+N)
print(f'Silver: {f(80)}\nGold: {f(256)}')