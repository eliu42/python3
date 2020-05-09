# 9.10 Generator Expressions

# Some simple generators can be coded succinclty as expressions using a syntax similar to list comprehensions but with parentheses instead of square brackets. These expressions are designed for situations where the generator is used right away by an enclosing function. Generator expressions are more compact but less versatile than full generator defintitions and tend to be more memory friendly than equivalent list comprehensions.

# Examples:

print(sum(i*i for i in range(10)))	# sum of squares

xvec = [10, 20, 30]
yvec = [7, 5, 3]
print(x*y for x,y in zip(xvec, yvec))	# dot product

unique_words = set(word for line in page for word in line.split())
valedictorian = max((student.gpa, student.name) for student in graduates)

data = 'golf'
list(data[i] for i in range(len(data) -1, -1, -1))