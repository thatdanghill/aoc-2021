import sys

file = open(sys.argv[1])
instructions = []
for line in file:
    spl = line.split()
    instr = spl[0] == 'on'
    coors = spl[1].split(',')
    xr = coors[0][2:].split('..')
    xtup = (int(xr[0]), int(xr[1]))
    yr = coors[1][2:].split('..')
    ytup = (int(yr[0]), int(yr[1]))
    zr = coors[2][2:].split('..')
    ztup = (int(zr[0]), int(zr[1]))
    instructions.append((instr, (xtup, ytup, ztup)))


def get_list_cubes(xrange, yrange, zrange, mincoord=None, maxcoord=None):
    cubelist = []
    for x in range(xrange[0], xrange[1]+1):
        for y in range(yrange[0], yrange[1] + 1):
            for z in range(zrange[0], zrange[1] + 1):
                if (mincoord is not None and maxcoord is not None and
                        (x < mincoord or x > maxcoord or y < mincoord  or y
                         > maxcoord or
                        z < mincoord or z > maxcoord)
                ):
                    continue
                cubelist.append((x,y,z))
    return cubelist


def has_overlap(cubeA, cubeB):
    x_overlap = not (cubeA[0][0] > cubeB[0][1] or cubeA[0][1] < cubeB[0][0])
    y_overlap = not (cubeA[1][0] > cubeB[1][1] or cubeA[1][1] < cubeB[1][0])
    z_overlap = not (cubeA[2][0] > cubeB[2][1] or cubeA[2][1] < cubeB[2][0])
    return x_overlap and y_overlap and z_overlap


def split_cube(to_split, cube):
    splits = []
    if to_split[0][0] < cube[0][0] <= to_split[0][1]:
        splits.append(
            (
                (
                    to_split[0][0],
                    cube[0][0] - 1
                ),
                to_split[1],
                to_split[2]
            )
        )
        to_split = (
            (
                cube[0][0],
                to_split[0][1]
            ),
            to_split[1],
            to_split[2]
        )
    if to_split[0][0] <= cube[0][1] < to_split[0][1]:
        splits.append(
            (
                (
                    cube[0][1] + 1,
                    to_split[0][1]
                ),
                to_split[1],
                to_split[2]
            )
        )
        to_split = (
            (
                to_split[0][0],
                cube[0][1]
            ),
            to_split[1],
            to_split[2]
        )
    if to_split[1][0] < cube[1][0] <= to_split[1][1]:
        splits.append(
            (
                to_split[0],
                (
                    to_split[1][0],
                    cube[1][0] - 1
                ),
                to_split[2]
            )
        )
        to_split = (
            to_split[0],
            (
                cube[1][0],
                to_split[1][1]
            ),
            to_split[2]
        )
    if to_split[1][0] <= cube[1][1] < to_split[1][1]:
        splits.append(
            (
                to_split[0],
                (
                    cube[1][1] + 1,
                    to_split[1][1]
                ),
                to_split[2]
            )
        )
        to_split = (
            to_split[0],
            (
                to_split[1][0],
                cube[1][1]
            ),
            to_split[2]
        )
    if to_split[2][0] < cube[2][0] <= to_split[2][1]:
        splits.append(
            (
                to_split[0],
                to_split[1],
                (
                    to_split[2][0],
                    cube[2][0] - 1
                )
            )
        )
        to_split = (
            to_split[0],
            to_split[1],
            (
                cube[2][0],
                to_split[2][1]
            )
        )
    if to_split[2][0] <= cube[2][1] < to_split[2][1]:
        splits.append(
            (
                to_split[0],
                to_split[1],
                (
                    cube[2][1] + 1,
                    to_split[2][1]
                )
            )
        )
    return splits


def add_ranges(on_cubes, cube):
    new_cubes = []
    for on_cube in on_cubes:
        if has_overlap(on_cube, cube):
            new_cubes += split_cube(on_cube, cube)
        else:
            new_cubes += [on_cube]
    return new_cubes


def execute_instructions(instructs, mincoord=None, maxcoord=None):
    on_list = []
    for instr, ranges in instructs:
        if mincoord is not None and maxcoord is not None:
            if (ranges[0][0] < mincoord or ranges[0][0] > maxcoord or
                ranges[0][1] < mincoord or ranges[0][1] > maxcoord or
                ranges[1][0] < mincoord or ranges[1][0] > maxcoord or
                ranges[1][1] < mincoord or ranges[1][1] > maxcoord or
                ranges[2][0] < mincoord or ranges[2][0] > maxcoord or
                ranges[2][1] < mincoord or ranges[2][1] > maxcoord
            ):
                continue
        if instr:
            new_on = [ranges]
            new_on += add_ranges(on_list, ranges)
            on_list = new_on
        else:
            on_list = add_ranges(on_list, ranges)
    return on_list


def number_on(on_list):
    return sum([
    (cube[0][1] - cube[0][0] + 1)*
    (cube[1][1] - cube[1][0] + 1)*
    (cube[2][1] - cube[2][0] + 1)
    for cube in on_list])


ex_50 = execute_instructions(instructions, -50, 50)
ex_full = execute_instructions(instructions)

print(f'Silver: {number_on(ex_50)}')
print(f'Gold: {number_on(ex_full)}')
