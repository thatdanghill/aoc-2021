import sys, math

file, = open(sys.argv[1])
x_part = file.split()[2]
y_part = file.split()[3]
x_vals = x_part.split('=')[1]
y_vals = y_part.split('=')[1]
x_range = (int(x_vals.split('..')[0]),int(x_vals.split('..')[1][:-1]))
y_range = (int(y_vals.split('..')[0]),int(y_vals.split('..')[1]))

max_depth = abs(y_range[0])
print(f'Silver: {max_depth*(max_depth-1)//2}')

min_x = math.ceil((math.sqrt(1 + 8*x_range[0]) - 1) / 2)
max_x = x_range[1]

min_y = y_range[0]
max_y = abs(y_range[0]) - 1

def hits_target(x_vel, y_vel):
    x_pos = y_pos = 0
    while True:
        x_pos += x_vel
        y_pos += y_vel
        if (x_range[0] <= x_pos <= x_range[1] and
                y_range[0] <= y_pos <= y_range[1]):
            return True
        elif (x_pos > x_range[1] or y_pos < y_range[0]):
            return False
        x_vel = max(x_vel - 1, 0)
        y_vel -= 1

num_combos = 0
for x in range(min_x, max_x+1):
    for y in range(min_y, max_y+1):
        if hits_target(x,y):
            num_combos += 1

print(f'Gold: {num_combos}')