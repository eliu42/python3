# 9.5 Inheritance

# Of course, a language feature would not be worthy of the name "class" without supporting interitance. The syntax for a derived class definition looks like this:

class DerivedClassName(BaseClassName):
	# <statement - 1>



	# <statement - N>

# The name BaseClassName must be defined in a scope containing the derived class definition. In place of a base class name, other arbitrary expressions are alsoi allowed. This can be useful, for example, when the base class is defined in another module:

class DerivedClassName(modname.BaseClassName):

# Exeuction of a derived class definition proceeds the same as for a base class. When the class object is constructed, the base class is remembered. This is is used for resolving attribute references: if a requested attribute is not foiund in the class, the search proceeds to look into the base class. This rule is applied recursively if the base class itself is derived from some other class.

# There's nothing special about instantiation of derived classes: DerivedClassName() creates a new instance of the class. Method references are resolved as follows: the corresonding class attribute is searched, descending down the chain of base classes if necessary, and the method reference is valid if this yeilds a function object.

# Derived classes may override methods of their base classes. Because methods have no special privileges when calling other methods of the same object, a method of a base class this calls another method defined in the same base class may end up calling a method of a derived class that overrides it. (for C++ programmers: all methods in Python are effectively 'virtual'.)

# An overriding method is a derived class may in fact want to extend rather than simply replace the base class method of the same name. There is a simple way to call the base class method directly: just call BaseClassName.methodname(self, arguments). This is occasionally useful to clients as well. (Note that this only works if the base class is accessible as BaseClassName in the global scope.)

# Python has two built-in functions that work with inheritance:

	# Use isinstanct() to check an instance's type: isinstance(obj,int) will be True only if obj.__class__is int or some class derived from int.
	# Use issubclass() to check class inheritance: issubclass(boot, int) is True since bool is a subclass of int. However, issubclass(float, int) is False since float is not a subclass of int.
