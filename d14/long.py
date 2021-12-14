import sys
from collections import defaultdict
template,_,*rule_strs = open(sys.argv[1])
template=template[:-1]
rules = {
    rule.split(' -> ')[0]: rule.split(' -> ')[1][:-1]
    for rule in rule_strs
}

def do_iterations(num):
    pair_counts = defaultdict(int)
    for i in range(len(template) - 1):
        pair = template[i:i + 2]
        pair_counts[pair] += 1

    for _ in range(num):
        new_pair_counts = defaultdict(int)
        for pair, count in pair_counts.items():
            if pair in rules:
                pair_a = pair[0] + rules[pair]
                pair_b = rules[pair] + pair[1]
                new_pair_counts[pair_a] += count
                new_pair_counts[pair_b] += count
        pair_counts = new_pair_counts

    letter_counts = defaultdict(int)
    for pair, count in pair_counts.items():
        letter_counts[pair[0]] += count
        letter_counts[pair[1]] += count

    letter_counts[template[0]] -= 1
    letter_counts[template[-1]] -= 1
    count_vals = letter_counts.values()
    return (max(count_vals) - min(count_vals))//2

print(f"Silver: {do_iterations(10)}\nGold: {do_iterations(40)}")




