import sys

file = open(sys.argv[1])
scan_list = []
scanner = None
for line in file:
    if '---' in line:
        scanner = []
    elif ',' in line:
        split_ln = line.split(',')
        scanner.append((int(split_ln[0]), int(split_ln[1]), int(split_ln[2])))
    else:
        scan_list.append(scanner)
scan_list.append(scanner)


def distance_map(beacons):
    dist_map = {}
    for i in range(len(beacons)):
        rowA = []
        bA = beacons[i]
        for j in range(len(beacons)):
            if j > i:
                bB = beacons[j]
                rowA.append((
                    bB[0] - bA[0],
                    bB[1] - bA[1],
                    bB[2] - bA[2]
                ))
        dist_map[bA] = rowA
    return dist_map


def get_rotations(beacon):
    x, y, z = beacon
    return [
        # No transform
        beacon,
        # rotate right
        (-y, x, z),
        # rotate left
        (y, -x, z),
        # rotate upside down
        (-x, -y, z),
        # turn right
        (-z, y, x),
        # turn right, rotate right
        (-y, -z, x),
        # turn right, rotate left
        (y, z, x),
        # turn right, rotate ud
        (z, -y, x),
        # turn left
        (z, y, -x),
        # turn left, rotate right
        (-y, z, -x),
        # turn left, rotate left
        (y, -z, -x),
        # turn left, rotate ud
        (-z, -y, -x),
        # turn up
        (x, -z, y),
        # turn up, rotate right
        (z, x, y),
        # turn up, rotate left
        (-z, -x, y),
        # turn up, rotate ud
        (-x, z, y),
        # turn down
        (x, z, -y),
        # turn down, rotate right
        (-z, x, -y),
        # turn down, rotate left
        (z, -x, -y),
        # turn down, rotate ud
        (-x, -z, -y),
        # turn backwards
        (-x, y, -z),
        # turn bw, rotate right
        (-y, -x, -z),
        # turn bw, rotate left
        (y, x, -z),
        # turn bw, rotate ud
        (x, -y, -z)
    ]

reverse_rotate = {
    0: 0,
    1: 2,
    2: 1,
    3: 3,
    4: 8,
    5: 18,
    6: 13,
    7: 7,
    8: 4,
    9: 14,
    10: 17,
    11: 11,
    12: 16,
    13: 6,
    14: 9,
    15: 15,
    16: 12,
    17: 10,
    18: 5,
    19: 19,
    20: 20,
    21: 21,
    22: 22,
    23: 23
}


def transform(beacon, rotation_num, offset):
    rotations = get_rotations(beacon)
    rotated = rotations[rotation_num]
    return (
        rotated[0] - offset[0],
        rotated[1] - offset[1],
        rotated[2] - offset[2]
    )


def test_transform(base_beacons, new_beacons, rotation_num, offset):
    num_matches = 0
    matched = []
    new_matched = []
    for beacon in new_beacons:
        if transform(beacon, rotation_num, offset) in base_beacons:
            num_matches += 1
            matched.append(transform(beacon, rotation_num, offset))
            new_matched.append(beacon)
        if num_matches >= 12:
            return True
    return False


def find_working_transform(base_beacons, new_beacons):
    base_dm = distance_map(base_beacons)
    new_dm = distance_map(new_beacons)

    for new_pt, new_dists in new_dm.items():
        for new_dist in new_dists:
            for base_pt, base_dists in base_dm.items():
                for base_dist in base_dists:
                    rotations = get_rotations(base_dist)
                    if new_dist in rotations:
                        rotation_number = rotations.index(new_dist)
                        reverse_rot = reverse_rotate[rotation_number]
                        rot_new_pt = get_rotations(new_pt)[reverse_rot]
                        offset = (
                            rot_new_pt[0] - base_pt[0],
                            rot_new_pt[1] - base_pt[1],
                            rot_new_pt[2] - base_pt[2]
                        )
                        if test_transform(base_beacons, new_beacons,
                                          reverse_rot, offset):
                            return reverse_rot, offset


def set_new_base(base_beacons, new_beacons):
    baseb = base_beacons.copy()
    trans = find_working_transform(baseb, new_beacons)
    if trans is None:
        return None
    rot, offset = trans
    for beacon in new_beacons:
        t_beac = transform(beacon, rot, offset)
        if t_beac not in base_beacons:
            baseb.append(t_beac)
    return baseb, (-offset[0], -offset[1], -offset[2])


base = scan_list[0]
leftovers = []
scan_positions = [(0,0,0)]
for i, scanner in enumerate(scan_list[1:]):
    maybe_new = set_new_base(base, scanner)
    if maybe_new is not None:
        base, offset = maybe_new
        scan_positions.append(offset)
        print(f'{i+1}: {len(base)}')
    else:
        print(f"Can't combine scanner {i+1}")
        leftovers.append(scanner)


while len(leftovers) != 0:
    print(f'Left: {len(leftovers)}')
    new_left = []
    for i, scanner in enumerate(leftovers):
        maybe_new = set_new_base(base, scanner)
        if maybe_new is not None:
            base, offset = maybe_new
            scan_positions.append(offset)
        else:
            new_left.append(scanner)
    leftovers = new_left

print(f'Silver: {len(base)}')

max_dist = 0
for i in range(len(scan_positions)):
    for j in range(len(scan_positions)):
        bA = scan_positions[i]
        bB = scan_positions[j]
        dist = abs(bA[0] - bB[0]) + abs(bA[1] - bB[1]) + abs(bA[2] - bB[2])
        if dist > max_dist:
            max_dist = dist

print(f'Gold: {max_dist}')

