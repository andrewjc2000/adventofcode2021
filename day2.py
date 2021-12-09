lines = open('day2.txt', 'r').readlines()

commands = [s.split() for s in lines]

directions = [(c[0], int(c[1])) for c in commands]

# part 1

x = 0
y = 0
aim = 0
for word, amount in directions:
    if word == 'forward':
        x += amount
    elif word == 'down':
        y += amount
    else:
        y -= amount

print(x * y)

# part 2

x = 0
y = 0
aim = 0
for word,amount in directions:
    if word == 'forward':
        x += amount
        y += aim * amount
    elif word == 'down':
        aim += amount
    else:
        aim -= amount

print(x * y)