lines = open('day7.txt', 'r').readlines()

nums = [int(a) for a in lines[0].split(',')]

min_sum_1 = float('inf')
min_sum_2 = float('inf')
for i in range(10000):
    # part 1 
    s_1 = sum([abs(a - i) for a in nums])
    # part 2
    s_2 = sum([abs(a - i)*(abs(a - i) + 1)//2 for a in nums])
    if s_1 < min_sum_1:
        min_sum_1 = s_1
    if s_2 < min_sum_2:
        min_sum_2 = s_2
print(min_sum_1)
print(min_sum_2)
