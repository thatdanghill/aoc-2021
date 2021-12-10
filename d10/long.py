import sys

file = open(sys.argv[1])
opposites = {
    '{': '}',
    '[': ']',
    '(': ')',
    '<': '>'
}
silver_pts = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}
gold_pts = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}
silver_score = 0
gold_scores = []
for line in file:
    closers = []
    corrupt = False
    for char in line[:-1]:
        if char in opposites:
            closers.append(opposites[char])
        elif char != closers.pop():
            silver_score += silver_pts[char]
            corrupt = True
            break
    if not corrupt:
        gold_score = 0
        for char in closers[::-1]:
            gold_score *= 5
            gold_score += gold_pts[char]
        gold_scores.append(gold_score)

gold_index = (len(gold_scores) - 1) // 2
print(f'Silver: {silver_score}\nGold: {sorted(gold_scores)[gold_index]}')