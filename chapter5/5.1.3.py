squares = []
for x in range(10):
	squares.append(x**2)

print(squares)


squares2 = [x**2 for x in range(10)]
print(squares2)


print([(x, y) for x in [1, 2, 3] for y in [3,1,4] if x != y])

combs = []
for x in [1,2,3]:
	for y in [3,1,4]:
		if x != y:
			combs.append((x, y))

print(combs)

# Flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
print([num for elem in vec for num in elem])

# List comprehensions can contain complex expressions and nested functions:

from math import pi
print([str(round(pi, i)) for i in range(1,6)]
