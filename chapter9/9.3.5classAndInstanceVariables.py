# 9.3.5 Class and Instance Variables

# Generally speaking, instance variables are for data unique to each instance and class varaibles are for attributes and methods shared by all instances of the class:

class Dog:

	kind = 'canine'

	def __init__(self, name):
		self.name = name

d = Dog('Fido')
e = Dog('Buddy')

print(d.kind)
print(e.kind)
print(d.name)
print(e.name)

# Need to look into variable/class redefinition

class Dog:
	tricks = []

	def __init__(self, name):
		self.name = name

	def add_trick(self, trick):
		self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)

# Correct design of the class should use an instance variable instead:

class Dog:

	def __init__(self, name):
		self.name = name
		self.tricks = []

	def add_trick(self, trick):
		self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)
print(e.tricks)
