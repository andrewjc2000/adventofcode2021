lines = open('day1.txt', 'r').readlines()

values = [int(l) for l in lines]

# part 1

print(len([i for i in range(1, len(values)) if values[i] > values[i-1]]))

# part 2

total = 0
prev = 0
curr = values[0] + values[1] + values[2] 
for i in range(0, len(values) - 3):
    prev = curr
    curr = prev - values[i] + values[i + 3]
    if curr > prev:
        total += 1
print(total)