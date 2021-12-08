import sys

file = open(sys.argv[1])
segs = [i.split('|') for i in file]
readings = [(i.split(), j.split()) for i,j in segs]

digit_1478 = 0
for _, display in readings:
    for digit in display:
        if len(digit) in [2, 3, 4, 7]:
            digit_1478 += 1

outputs = []
for sigs, display in readings:
    sig_map = {}
    for sig in sigs:
        sabc = ''.join(sorted(sig))
        if len(sig) == 2:
            sig_map[1] = sabc
        if len(sig) == 3:
            sig_map[7] = sabc
        if len(sig) == 4:
            sig_map[4] = sabc
        if len(sig) == 7:
            sig_map[8] = sabc

    for sig in sigs:
        sabc = ''.join(sorted(sig))
        if len(sig) == 5:
            if all([i in sabc for i in sig_map[1]]):
                sig_map[3] = sabc
            elif all([i in sabc for i in set(sig_map[4])-set(sig_map[1])]):
                sig_map[5] = sabc
            else:
                sig_map[2] = sabc
        if len(sig) == 6:
            if any([i not in sabc for i in sig_map[1]]):
                sig_map[6] = sabc
            elif all([i in sabc for i in set(sig_map[4])-set(sig_map[1])]):
                sig_map[9] = sabc
            else:
                sig_map[0] = sabc

    rev_sig_map = {v: k for k, v in sig_map.items()}
    outputs.append(int(''.join([str(rev_sig_map[''.join(sorted(i))]) for i
                                in display])))

print(f'Silver: {digit_1478}\nGold: {sum(outputs)}')


