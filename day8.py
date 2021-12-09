lines = open('day8.txt', 'r').readlines()

halves = [line.split(' | ') for line in lines]

# part 1

print(sum([len([w for w in line[1].split() if len(w) in {2, 3, 4, 7}]) for line in halves]))

# part 2

def sorted_string(s):
    chars = list(s)
    chars.sort()
    return ''.join(chars)

s = 0

for line in halves:
    # 1, 7, 4, 8, 2, 3, 5, 6
    inp, out = line[0].split(), line[1].split()
    one_rep = [w for w in inp if len(w) == 2][0]
    seven_rep = [w for w in inp if len(w) == 3][0]
    four_rep = [w for w in inp if len(w) == 4][0]
    eight_rep = [w for w in inp if len(w) == 7][0]
    a_rep = [c for c in 'abcdefg' if c in seven_rep and c not in one_rep][0]
    # 8 - 9 = {e}
    # 8 - 6 = {c}
    # 8 - 0 {d}
    six_long = [w for w in inp if len(w) == 6]
    diffs = [list(set(eight_rep) - set(curr))[0] for curr in six_long]
    c_rep = [c for c in 'abcdefg' if c in diffs and c in one_rep][0]
    f_rep = [c for c in 'abcdefg' if c is not c_rep and c in one_rep][0]
    # 5 long: 2, 3, 5
    two_rep = [w for w in inp if len(w) == 5 and f_rep not in w][0]
    three_rep = [w for w in inp if len(w) == 5 and w is not two_rep and c_rep in w][0]
    e_rep = [c for c in 'abcdefg' if c in two_rep and c not in three_rep][0]
    five_rep = [w for w in inp if len(w) == 5 and w is not three_rep and w is not two_rep][0]
    six_rep = [w for w in six_long if c_rep not in w][0]
    zero_rep = [w for w in six_long if e_rep in w and w is not six_rep][0]
    nine_rep = [w for w in six_long if e_rep not in w and w is not six_rep][0]
    sorted_vals = [zero_rep, one_rep, two_rep, three_rep, four_rep, five_rep, six_rep, seven_rep, eight_rep, nine_rep]
    sorted_vals = [sorted_string(s) for s in sorted_vals]
    # print(sorted_vals, out)
    s += int(''.join([str(sorted_vals.index(sorted_string(s))) for s in out]))
print(s)