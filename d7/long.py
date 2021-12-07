import sys
file,=open(sys.argv[1])
crab_pos = [int(i) for i in file.split(',')]
#crab_pos = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
crab_pos=sorted(crab_pos)
med=crab_pos[len(crab_pos)//2]
fuel_1 = sum([abs(pos-med) for pos in crab_pos])
avg = sum(crab_pos)/len(crab_pos)
find_fuel=lambda x: sum([0.5*abs(i-x)*(abs(i-x)+1) for i in crab_pos])
fuel_2 = min(find_fuel(avg//1), find_fuel(-(-avg//1)))
print(f'Silver: {fuel_1}\nGold: {fuel_2}')