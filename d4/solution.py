import sys

order,_,*rest = open(sys.argv[1]).readlines()

acc = []
bcc = []
i = 0
for line in rest:
    if i%6 == 5:
        acc.append(bcc)
        bcc = []
    else:
        bcc.append([int(n) for n in line.split()])
    i+=1

order = [int(i) for i in order.split(',')]

def calculate_score(board, bitmap):
    antibit = [[not val for val in row] for row in bitmap]
    return sum([sum([v1*v2 for v1,v2 in zip(r1,r2)]) for r1,r2 in zip(board,
                                                                      antibit)])


def run_bingo(boards):
    bitmaps = [[[0 for _ in l2] for l2 in l1] for l1 in boards]
    for num in order:
        for bi, board in enumerate(boards):
            for ci, col in enumerate(board):
                for ri, val in enumerate(col):
                    if val == num:
                        bitmaps[bi][ci][ri] = 1

            row_totals = [sum(row) for row in bitmaps[bi]]
            col_totals = [sum(col) for col in zip(*bitmaps[bi])]
            if (5 in row_totals) or (5 in col_totals):
                return num*calculate_score(board, bitmaps[bi])

def run_last_bingo(boards):
    bitmaps = [[[0 for _ in l2] for l2 in l1] for l1 in boards]
    for num in order:
        topop = []
        for bi, board in enumerate(boards):
            for ci, col in enumerate(board):
                for ri, val in enumerate(col):
                    if val == num:
                        bitmaps[bi][ci][ri] = 1
            row_totals = [sum(row) for row in bitmaps[bi]]
            col_totals = [sum(col) for col in zip(*bitmaps[bi])]
            if (5 in row_totals) or (5 in col_totals):
                topop.append(bi)

        if len(boards) == 1 and len(topop) == 1:
            print(boards[0])
            print(bitmaps[0])
            print(num)
            return num*calculate_score(boards[0], bitmaps[0])

        boards = [b for i,b in enumerate(boards) if i not in topop]
        bitmaps = [b for i,b in enumerate(bitmaps) if i not in topop]

print(run_bingo(acc.copy()))
print(run_last_bingo(acc.copy()))