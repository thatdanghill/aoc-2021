import sys

A = [[int(i) for i in line[:-1]] for line in open(sys.argv[1])]

def get_neighbors(x,y):
    neighbor_pos = []
    x_left = x > 0
    x_right = x < 9
    y_up = y > 0
    y_down = y < 9
    if x_left:
        neighbor_pos.append((x-1, y))
    if x_right:
        neighbor_pos.append((x+1, y))
    if y_up:
        neighbor_pos.append((x, y-1))
    if y_down:
        neighbor_pos.append((x, y+1))
    if x_left and y_up:
        neighbor_pos.append((x - 1, y-1))
    if x_left and y_down:
        neighbor_pos.append((x - 1, y+1))
    if x_right and y_up:
        neighbor_pos.append((x + 1, y-1))
    if x_right and y_down:
        neighbor_pos.append((x + 1, y+1))
    return neighbor_pos


def flash(x,y):
    num_flashes = 1
    for x1, y1 in get_neighbors(x, y):
        A[y1][x1] += 1
        if A[y1][x1] == 10:
            num_flashes += flash(x1,y1)
    return num_flashes

def do_step():
    num_flashes = 0
    for i in range(100):
        x,y = i%10, i//10
        A[y][x] += 1
        if A[y][x] == 10:
            num_flashes += flash(x,y)
    for i in range(100):
        x, y = i % 10, i // 10
        if A[y][x] > 9:
            A[y][x] = 0
    return num_flashes


flashes = 0
steps = 0
while A != [[0]*10]*10:
    steps += 1
    flashes += do_step()
    if steps == 100:
        print(f'Silver: {flashes}')

print(f'Gold: {steps}')