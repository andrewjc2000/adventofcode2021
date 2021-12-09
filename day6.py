lines = open('day6.txt', 'r').readlines()

nums = [int(s) for s in lines[0].split(',')]

og_map = {}

for i in nums:
    if i not in og_map.keys():
        og_map[i] = 1
    else:
        og_map[i] += 1

# both parts
for x in [80, 256]:
    count_map = {k: og_map[k] for k in og_map.keys()}
    for i in range(x):
        new_map = {}
        for j in range(1, 9):
            if j in count_map.keys():
                new_map[j - 1] = count_map[j]
        if 0 in count_map.keys():
            extra1 = new_map[8] if 8 in new_map.keys() else 0
            new_map[8] = count_map[0] + extra1
            extra2 = new_map[6] if 6 in new_map.keys() else 0
            new_map[6] = count_map[0] + extra2
        count_map = new_map

    print(sum([count_map[k] for k in count_map.keys()]))