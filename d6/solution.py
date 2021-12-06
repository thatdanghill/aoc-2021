import sys
file, = open(sys.argv[1])
init_fish = [int(i) for i in file.split(',')]
def count_fish(gens):
    old_fish = [init_fish.count(i) for i in range(7)]
    new_fish = [0] * 9
    for _ in range(gens):
        old_fish = old_fish[1:] + [old_fish[0] + new_fish[0]]
        new_fish = new_fish[1:] + [old_fish[6]]
    return sum(old_fish + new_fish)
print(f'Silver: {count_fish(80)}\nGold: {count_fish(256)}')

