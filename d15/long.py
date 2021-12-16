import sys

def get_neighbors(x,y,max_val):
    neighbors = []
    if x > 0:
        neighbors.append((x-1, y))
    if x < max_val:
        neighbors.append((x + 1, y))
    if y > 0:
        neighbors.append((x, y-1))
    if y < max_val:
        neighbors.append((x, y + 1))
    return neighbors

def min_frontier(frontier, cost_map):
    min_path = float('inf')
    min_front = None
    for x,y in frontier:
        if cost_map[y][x] < min_path:
            min_path = cost_map[y][x]
            min_front = (x,y)
    return min_front

def run_path(grid):
    inf = float('inf')
    grid_len = len(grid)
    cost_map = [[inf]*grid_len for _ in range(grid_len)]
    cost_map[0][0] = 0
    frontier = [(0,0)]

    while cost_map[-1][-1] == inf:
        cur_pt = min_frontier(frontier, cost_map)
        frontier.remove(cur_pt)
        for x,y in get_neighbors(*cur_pt, grid_len-1):
            if cost_map[y][x] == inf:
                cost_map[y][x] = cost_map[cur_pt[1]][cur_pt[0]] + grid[y][x]
                frontier.append((x,y))
    return cost_map[-1][-1]

def append_horiz(tile_list):
    total_tile = []
    for row_num in range(len(tile_list[0])):
        row = [val for tile in tile_list for val in tile[row_num]]
        total_tile.append(row)
    return total_tile

def append_vert(tile_list):
    return [row for tile in tile_list for row in tile]

def offset_tile(tile, offset):
    return [[(val + offset - 1)%9 + 1 for val in row] for row in tile]


tile_1 = [[int(i) for i in line[:-1]] for line in open(sys.argv[1])]

five_by_five = append_vert([
    append_horiz([
        offset_tile(tile_1, i+j) for i in range(5)
    ]) for j in range(5)
])

print(f'Silver: {run_path(tile_1)}\nGold: {run_path(five_by_five)}')

