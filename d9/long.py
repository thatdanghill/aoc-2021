import sys
A = [int(j) for i in open(sys.argv[1]) for j in i[:-1]]
safety_score = 0

def get_neighbor_positions(i):
    neighbor_pos = []
    if (i + 1) % 100 != 0:
        neighbor_pos.append(i + 1)
    if (i - 1) % 100 != 99:
        neighbor_pos.append(i - 1)
    if (i - 100) >= 0:
        neighbor_pos.append(i - 100)
    if (i + 100) < 10 ** 4:
        neighbor_pos.append(i + 100)
    return neighbor_pos

for i, reading in enumerate(A):
    if all([reading < A[k] for k in get_neighbor_positions(i)]):
        safety_score += reading + 1

basins = []
all_pos = list(range(10**4))
removed = []
while len(all_pos) != 0:
    i = all_pos[0]
    all_pos.remove(i)
    removed.append(i)
    if A[i] != 9:
        basin = [i]
        to_try = [k for k in get_neighbor_positions(i) if k in all_pos]
        while len(to_try) != 0:
            j = to_try[0]
            to_try.remove(j)
            all_pos.remove(j)
            removed.append(j)
            if A[j] != 9:
                basin.append(j)
                to_try += [k for k in get_neighbor_positions(j) if k in
                           all_pos and k not in to_try]

        basins.append(basin)

basin_sizes = sorted([len(i) for i in basins])
print(f'Silver: {safety_score}\nGold: {basin_sizes[-3]*basin_sizes[-2]*basin_sizes[-1]}')
