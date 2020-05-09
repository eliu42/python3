# Programs may name their own exceptions by creating a new exception class (see Classes) for more about Python classes). Exceptions should typically be derived from the Exception class, either directly or indirectly.

# Exception classes can be defined which do anything any other class can do, but are usually kept simple, often only offering a number of attributes that allow information about the error to be extracted by handlers for the exception. When creating a module that can raise several distinct errors, a common practice is to create a base class for exceptions defined by that module, and subclass that to create specific classes for different error conditions:

class Error(Exception):
	"""Base class for exceptions in this module."""
	pass

class InputError(Error):
	"""Exception raised for errors in the input.

	Attributes:
		expression -- input expression in which the error occurred
		message -- explanation of the error
	"""

	def __init__(self, expression, message):
		self.expression = expression
		self.message = message


try:
	raise InputError('Error World', 'something wasn\' quite right')
except InputError:
	print('This is an input error!')
	raise

#  Most exceptions are defined with names that end in "Error", similar to the naming of the standard exceptions.

# Many standard modules define their own exceptions to report errors that may occur in functions they define. More information on classes is presented in chapter https://docs.python.org/3/tutorial/classes.html#tut-classes.
