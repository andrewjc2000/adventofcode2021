lines = open('day3.txt', 'r').readlines()
lines_copy = [line.strip() for line in lines]

total = len(lines)

# part 1

counts = [sum([1 for line in lines if line[i] == '1']) for i in range(12)]
gamma = int(''.join([str(int(i >= 500)) for i in counts]), 2)
epsilon = int(''.join([str(int(i < 500)) for i in counts]), 2)

print(gamma * epsilon)

# part 2

for i in range(12):
    count = sum([1 for line in lines if line[i] == '1'])
    total = len(lines)
    if count == total/2:
        lines = [line for line in lines if line[i] == '1']
    else:
        lines = [line for line in lines if line[i] == '01'[int(count > total / 2)]]
oxygen_rating = int(lines[0], 2)

lines = lines_copy
i = 0
while len(lines) > 1:
    count = sum([1 for line in lines if line[i] == '1'])
    total = len(lines)
    if count == total/2:
        lines = [line for line in lines if line[i] == '0']
    else:
        lines = [line for line in lines if line[i] == '01'[int(count < total / 2)]]
    i += 1

co2_rating = int(lines[0], 2) 

print(oxygen_rating * co2_rating)