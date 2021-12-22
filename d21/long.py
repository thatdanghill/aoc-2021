import sys

p1_str, p2_str = open(sys.argv[1])
p1_start = int(p1_str.split(':')[-1])
p2_start = int(p2_str.split(':')[-1])

p1_space = p1_start
p2_space = p2_start

p1_score = p2_score = 0
rolls = 0
dice = 1
while p1_score < 1000 and p2_score < 1000:
    # Player 1 rolls
    rolls += 3
    roll_score = dice + dice % 100 + (dice + 1) % 100 + 2
    dice = (dice + 2) % 100 + 1
    p1_space = (p1_space + roll_score - 1) % 10 + 1
    p1_score += p1_space
    if p1_score >= 1000:
        print(f'Silver: {p2_score * rolls}')

    # Player 2 rolls
    rolls += 3
    roll_score = dice + dice % 100 + (dice + 1) % 100 + 2
    dice = (dice + 2) % 100 + 1
    p2_space = (p2_space + roll_score - 1) % 10 + 1
    p2_score += p2_space
    if p2_score >= 1000:
        print(f'Silver: {p1_score * rolls}')


uni_combos = {
    3: 1,
    4: 3,
    5: 6,
    6: 7,
    7: 6,
    8: 3,
    9: 1
}


def get_win_paths(cur_pos, cur_score=0, cur_path='', cur_unis=1):
    if cur_score >= 21:
        return {cur_path: cur_unis}
    dict_list = [
        get_win_paths(
            (cur_pos + i - 1) % 10 + 1,
            cur_score + (cur_pos + i - 1) % 10 + 1,
            cur_path + str(i),
            cur_unis * uni_combos[i]
        )
        for i in range(3, 10)
    ]
    return {
        k: v
        for d in dict_list
        for k, v in d.items()
    }


def get_win_length_count(cur_pos):
    win_paths = get_win_paths(cur_pos)
    len_unis = {}
    for path, unis in win_paths.items():
        pathlen = len(path)
        if pathlen in len_unis:
            len_unis[pathlen] += unis
        else:
            len_unis[pathlen] = unis
    return len_unis


def num_unis(path_str):
    num_unis = 0
    for i in path_str:
        num_unis += uni_combos[int(i)]
    return num_unis


def get_win_unis(p1_pos, p2_pos):
    p1_wp = get_win_length_count(p1_pos)
    p2_wp = get_win_length_count(p2_pos)

    p1_wunis = 0
    p1_min_path = min(p1_wp.keys())
    p1_max_path = max(p1_wp.keys())
    for i in range(p1_min_path, p1_max_path + 1):
        sum_p2_wins = sum([
            p2_wp.get(j, 0)*int(27**(i - 1 - j))
            for j in range(i)])
        p1_wunis += p1_wp[i] * (27**(i-1) - sum_p2_wins)

    p2_wunis = 0
    p2_min_path = min(p2_wp.keys())
    p2_max_path = max(p2_wp.keys())
    for i in range(p2_min_path, p2_max_path + 1):
        sum_p1_wins = sum(
            [p1_wp.get(j, 0) * int(27 ** (i - j)) for j in range(i+1)])
        p2_wunis += p2_wp[i] * (27**i - sum_p1_wins)
    return p1_wunis, p2_wunis

print(f'Gold: {max(*get_win_unis(p1_start, p2_start))}')