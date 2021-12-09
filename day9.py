lines = open('day9.txt', 'r').readlines()
lines = [[int(c) for c in line.strip()] for line in lines]

def is_low_point(row, col):
    for i in range(0, 3):
        for j in range(0, 3):
            if (i + j) % 2 == 1:
                r, c = row + i - 1, col + j - 1
                if r >= 0 and c >= 0 and r < len(lines) and c < len(lines[0]):
                    if lines[r][c] <= lines[row][col]:
                        return False
    return True

# part 1

s = 0

coords = set()
for row in range(len(lines)):
    for col in range(len(lines[0])):
        if is_low_point(row, col):
            s += lines[row][col] + 1

print(s)

# part 2

def num_points(r, c):
    visited = set()
    stack = [(r, c)]
    while len(stack) > 0:
        row, col = stack.pop()
        visited.add((row, col))
        for i in range(0, 3):
            for j in range(0, 3):
                if (i + j) % 2 == 1:
                    r, c = row + i - 1, col + j - 1
                    if (r, c) not in visited and r >= 0 and c >= 0 and r < len(lines) and c < len(lines[0]):
                        if lines[r][c] != 9:
                            stack.append((r, c))
    return len(visited)


basin_sizes = []
for row in range(len(lines)):
    for col in range(len(lines[0])):
        if is_low_point(row, col):
            basin_sizes.append(num_points(row, col))

basin_sizes.sort()
print(basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3])