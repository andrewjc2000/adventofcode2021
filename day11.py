lines = open('day11.txt', 'r').readlines()
nums = [[int(c) for c in line.strip()] for line in lines]
og = [[c for c in line] for line in nums]

# part 1

c = 0

def is_valid(x, y):
    return x >= 0 and y >= 0 and x < 10 and y < 10

for iterations in range(100):
    for y in range(10):
        for x in range(10):
            nums[y][x] += 1
    found = True
    big_flashing = set()
    while found:
        found = False
        flashing = []
        for y in range(10):
            for x in range(10):
                if nums[y][x] > 9:
                    c += 1
                    nums[y][x] = 0
                    flashing.append((y, x))
                    big_flashing.add((y, x))
                    found = True
        for y, x in flashing:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if (i, j) != (0, 0) and is_valid(y + i, x + j) and (y + i, x + j) not in big_flashing:
                        nums[y + i][x + j] += 1

print(c)

# part 2

nums = og
iterations = 0
while True:
    iterations += 1
    for y in range(10):
        for x in range(10):
            nums[y][x] += 1
    found = True
    big_flashing = set()
    while found:
        found = False
        flashing = []
        for y in range(10):
            for x in range(10):
                if nums[y][x] > 9:
                    c += 1
                    nums[y][x] = 0
                    flashing.append((y, x))
                    big_flashing.add((y, x))
                    found = True
        for y, x in flashing:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if (i, j) != (0, 0) and is_valid(y + i, x + j) and (y + i, x + j) not in big_flashing:
                        nums[y + i][x + j] += 1
    if len(big_flashing) == 100:
        print(iterations)
        break