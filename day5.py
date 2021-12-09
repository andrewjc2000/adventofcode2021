lines = open('day5.txt', 'r').readlines()

coords = [[[int(a) for a in coord.strip().split(',')] for coord in line.split('->')] for line in lines]

vertical = [line for line in coords if line[0][0] == line[1][0]]
horizontal = [line for line in coords if line[0][1] == line[1][1]]
set_coords = set([((line[0][0], line[0][1]), (line[1][0], line[1][1])) for line in coords])
set_h = set([((line[0][0], line[0][1]), (line[1][0], line[1][1])) for line in horizontal])
set_v = set([((line[0][0], line[0][1]), (line[1][0], line[1][1])) for line in vertical])
diagonal = (set_coords - set_h) - set_v
diagonal = [[line[1], line[0]] if line[0][0] > line[1][0] else line for line in diagonal]
vertical = [[line[1], line[0]] if line[1][1] < line[0][1] else line for line in vertical]
horizontal = [[line[1], line[0]] if line[1][0] < line[0][0] else line for line in horizontal]

max_x = max([max(x[0][0], x[1][0]) for x in coords])
max_y = max([max(x[0][1], x[1][1]) for x in coords])
grid = [[0]*1000 for x in range(1000)]

for line in horizontal:
	for x in range(line[0][0], line[1][0] + 1):
		grid[x][line[0][1]] += 1
for line in vertical:
	for y in range(line[0][1], line[1][1] + 1):
		grid[line[0][0]][y] += 1

# part 1

print(sum([len([x for x in line if x >= 2]) for line in grid]))

for line in diagonal:
	top_left = line[0][1] <= line[1][1]
	i = 0
	for x in range(line[0][0], line[1][0] + 1):
		grid[x][line[0][1] + i] += 1
		i += 1 if top_left else -1

# part 2

print(sum([len([x for x in line if x >= 2]) for line in grid]))