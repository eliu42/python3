# If the same attribute name occurs in both an instance and in a class, then attribute lookup prioritizes the instance:

class Warehouse:
	purpose = 'storage'
	region = 'west'

w1 = Warehouse()
print(w1.purpose, w1.region)
w2 = Warehouse()
w2.region = 'east'
print(w2.purpose, w2.region)

# Data attributes may be referenced by methods as well as ordinary users ("clients") of an object. In other words, classes are not usable to implement pure abstract data types. In fact, nothing in Python makes it possible to enforce data hiding - it is all based upon convention. (On the other hand, the Python implementation, written in C, can completely hide implementation details and control access to an object if necessary; this can be used by extentions to Python written in C.).

# Clients should use data attributes with care - clients may mess up invariants maintained by the methods by stamping on their data attributes. Note that clients may add data attributes of their own an instance object without affecting the validitiy of the methods as long as name conflicts are avoided - again, a naming convention can save a lot of headaches here.

# There is no shorthand for referencing data attributes (or other methods!) from within methods. I find that this actually increases the readilibity of methods: there is no chance of confusing local variables and instance variables when glancing through a method.

# Often the first argument of a method is called self. This is nothing more than a convention: the name self has absolutely no special meaning to Python. Note, however, that by not following the convention your code may be less readable to other Python programmers, and it is also conceivable that a class browser program might be written that relies upon such a convention.

# Any function object that is a class attribute defines a method for instances of that class. It is not necessary that the function definition is textually enclosed in the class defintion: assigning a function object to a local variable in the class is also ok. For example:

## Function defined outside the class

def f1(self, x, y):
	return min(x, x+y)

class C:
	f = f1

	def g(self):
		return 'hello world'

	h = g

# Now f, g, and h are all attributes of class C that refer to function objects, and consequently they are all methods of instances of C - h being exactly equivalent to g. Note that this practice usually only serves to confuse the reader of a program.

# Methods may call other methods by using methods attributes of the 'self' argument:

c = C()
print(c.g())
print(c.f(1, 2))


class Bag:
	def __init__(self):
		self.data = []

	def add(self, x):
		self.data.apppend(x)

	def addtwice(self, x):
		self.add(x)
		self.add(x)

# Methods may reference global names in the same way as ordinary functions. the global scope associated with a method is the module containing its definition. (A class is never used as a global scope.) While one rarely encounters a good reason for using global data in a method, there are many legitimate uses of the global scope: for one thing, functions and modules imported into the global scope can be used by methods, as well as functions and classes defined in it. Usually the class containing the method is itself defined in this global scope, and in the next section we'll find some good reasons why a method would want to reference its own class.

# Each value is an object, and therefore has a class (also called its type). It is stored as object.__class__.
