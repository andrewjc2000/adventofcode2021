lines = open('table.txt', 'r').readlines()

def padded(s, paddings):
    return ' '*paddings[0] + s.ljust(paddings[1]-paddings[0])

max_day = len(lines)

for line in lines:
    values = line.split()
    values = [s.strip() for s in values]

    # before, then total
    paddings = [[1, 42], [3, 15], [5, 15], [8, 16], [3, 15], [5, 15], [8, 16]]

    day = int(values[0])
    part1 = '[%d](https://adventofcode.com/2021/day/%d)' % (day, day)
    part2 = '[Day %d Solution](https://github.com/andrewjc2000/adventofcode2021/blob/main/day%d.py)' % (day, day)

    extra = 2 if max_day >= 10 else 3

    paddings = [[1, len(part1) + extra], [3, 15], [5, 15], [8, 16], [3, 15], [5, 15], [8, 16], [1, len(part2) + extra]]

    words = [part1] + values[1:] + [part2]
    print('|' + '|'.join([padded(words[i], paddings[i]) for i in range(len(words))]) + '|')