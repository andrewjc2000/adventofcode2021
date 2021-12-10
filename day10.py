lines = open('day10.txt', 'r').readlines()

s = 0
m = {')': 3, ']': 57, '}': 1197, '>': 25137}

scores = []

for line in lines:
	chars = [c for c in line]
	stack = []
	corrupted = False
	# constructing the stack, adding to s done for part 1
	for c in line.strip():
		if c in '([{<':
			stack.append(c)
		else:
			if len(stack) == 0:
				s += m[c]
				break
			else:
				index1 = '([{<'.index(stack.pop())
				index2 = ')]}>'.index(c)
				if index1 != index2:
					s += m[c]
					corrupted = True
					break
	# if the stack is not empty and it's not corrupted, do part 2 stuff!
	if len(stack) != 0 and not corrupted:
		score = 0
		for c in stack[::-1]:
			value = '([{<'.index(c) + 1
			score = 5 * score + value
		scores.append(score)
scores.sort()
# part 1 output
print(s)
# part 2 output
print(scores[len(scores)//2])
