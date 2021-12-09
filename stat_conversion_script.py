values = input().split()
values = [s.strip() for s in values]

def padded(s, paddings):
    return ' '*paddings[0] + s.ljust(paddings[1]-paddings[0])


# before, then total
paddings = [[1, 42], [3, 15], [5, 15], [8, 16], [3, 15], [5, 15], [8, 16]]

day = int(values[0])
part1 = '[%d](https://adventofcode.com/2021/day/%d)' % (day, day)
words = [part1] + values[1:]
print('|' + '|'.join([padded(words[i], paddings[i]) for i in range(len(words))]) + '|')