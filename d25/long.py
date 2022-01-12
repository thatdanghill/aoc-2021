import sys
import copy

file = open(sys.argv[1])
bed = [[c for c in line[:-1]] for line in file]

def step(grid):
    width = len(grid[0])
    height = len(grid)
    new_grid = copy.deepcopy(grid)
    num_moves = 0
    for j, row in enumerate(grid):
        for i, spot in enumerate(row):
            if spot == '>':
                if grid[j][(i + 1) % width] == '.':
                    new_grid[j][i] = '.'
                    new_grid[j][(i+1) % width] = '>'
                    num_moves += 1
    newer_grid = copy.deepcopy(new_grid)
    for j, row in enumerate(grid):
        for i, spot in enumerate(row):
            if spot == 'v':
                if new_grid[(j+1) % height][i] == '.':
                    newer_grid[j][i] = '.'
                    newer_grid[(j+1) % height][i] = 'v'
                    num_moves += 1

    return newer_grid, num_moves

moves = 1
its = 0
while moves > 0:
    bed, moves = step(bed)
    print(f'{its}:')
    for row in bed:
        print(''.join(row))
    print('\n')
    its += 1

print(its)
