import sys
file = open(sys.argv[1])
points = []
instructions = []
for line in file:
    if 'fold along' in line:
        splt = line.split('=')
        instructions.append((splt[0][-1]=='y', int(splt[1])))
    elif len(line) > 1:
        splt = line.split(',')
        points.append((int(splt[0]), int(splt[1])))

silver = 0
for i, (dim, fold) in enumerate(instructions):
    new_points = set()
    for point in points:
        if point[dim] < fold:
            new_points.add(point)
        elif point[dim] > fold:
            new_point = [0,0]
            new_point[dim] = 2 * fold - point[dim]
            new_point[~dim] = point[~dim]
            new_points.add(tuple(new_point))
    points = new_points
    if i == 0:
        silver = len(points)
    i += 1
print(f'Silver: {silver}')


xmax = max([p[0] for p in points]) + 1
ymax = max([p[1] for p in points]) + 1

dotmap = [[' ']*xmax for _ in range(ymax)]
for x,y in points:
    dotmap[y][x] = '#'
for row in dotmap:
    print(''.join(row))