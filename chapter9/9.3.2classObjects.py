# 9.3.2 Class Object

# Class objects support two kind of operations: attribute references and instantiation.
# Attribute references use the standard syntax used for all attribute references in Python: obj.name. Valid attribute names are all the names that were in the class's namespace when the class object was created. So, if the class definition looked like this:

class MyClass:
	"""A simple example class"""
	i = 12345

	def f(self):
		return 'hello world'

# Then MyClass.i and MyClass.f are valid attribute references, returning an integer and a function object, respsectively. Class attributes can also be asigned to, so you can change the value of MyClass.i by assignement. _doc_ is also a valid attribute, returning the docstring belonging to the class: "A simple example class".

# Class instantiation uses function notation. Just pretend that the class object is a parameter less function that returns a new instance of the class. For example (assuming the ahove class):

x = MyClass()

# Creates a new instance of the class and assigns this object to the local variable x.

# The instantiation operation ("calling" a class object) creates an empty object. Many classes like to create objects with instances customized to a specific intial state. Therefore a class may define a special method named _init_(), like this:

def __init__(self):
	self.data = []

# When a class defines an __init__() method, class instantiation automatically invokes __init__() for the newly-created class instance. So in this example, a new, initialized instance can be obtained by:

x = MyClass()

# Of course, the __init__() method may have arguments for greater flexibility. In that case, arguments given to the class instantiation operator are passed on to __init__(). For example,

class Complex:
	def __init__(self, realpart, imagpart):
		self.r = realpart
		self.i = imagpart

x = Complex(3.0, -4.5)
#Note, python3 does not print parentheses
print(x.r, x.i)
