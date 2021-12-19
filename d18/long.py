import sys


def get_from_path(num, path):
    curnum = num
    for ind in path:
        curnum = curnum[ind]
    return curnum

def increase_from_path(num, path, val):
    curnum = num
    for ind in path[:-1]:
        curnum = curnum[ind]
    curnum[path[-1]] += val
    return num

def set_from_path(num, path, val):
    curnum = num
    for ind in path[:-1]:
        curnum = curnum[ind]
    curnum[path[-1]] = val
    return num

def get_all_paths(num, prefix=[]):
    if isinstance(num, int):
        return [prefix]
    else:
        return (get_all_paths(num[0], prefix + [0]) +
                get_all_paths(num[1], prefix + [1]))

def detect_explode(num):
    for path in get_all_paths(num):
        if len(path) > 4:
            return True, path[:-1]
    return False, None

def detect_split(num):
    for path in get_all_paths(num):
        if get_from_path(num, path) > 9:
            return True, path
    return False, None

def explode(num, path):
    all_paths = get_all_paths(num)
    ind = all_paths.index(path + [0])
    shortlist = get_from_path(num, path)
    if ind != 0:
        num = increase_from_path(num, all_paths[ind - 1], shortlist[0])
    if ind != len(all_paths) - 2:
        num = increase_from_path(num, all_paths[ind + 2], shortlist[1])
    return set_from_path(num, path, 0)

def split(num, path):
    splitnum = get_from_path(num, path)
    lower = splitnum // 2
    upper = -(-splitnum // 2)
    return set_from_path(num, path, [lower, upper])

def reduce_snail_num(num):
    is_reduced = False
    while not is_reduced:
        needs_explode, explode_pos = detect_explode(num)
        needs_split, split_pos = detect_split(num)
        if needs_explode:
            num = explode(num, explode_pos)
        elif needs_split:
            num = split(num, split_pos)
        else:
            is_reduced = True
    return num

def find_magnitude(num):
    if isinstance(num, int):
        return num
    return 3 * find_magnitude(num[0]) + 2 * find_magnitude(num[1])

file = open(sys.argv[1]).readlines()
snail_num = None
for line in file:
    if snail_num is None:
        snail_num = eval(line)
    else:
        snail_num = reduce_snail_num([snail_num, eval(line)])

print(f'Silver: {find_magnitude(snail_num)}')

max_magnitude = 0
for i in range(len(file)):
    for j in range(len(file)):
        if i != j:
            mag = find_magnitude(
                reduce_snail_num(
                    [eval(file[i]), eval(file[j])]))
            if mag > max_magnitude:
                max_magnitude = mag

print(f'Gold: {max_magnitude}')