# The raise statement allows the programmer to force a specified exception to occur. For example:
# Only works in interactive mode. Lots of things only work in interactive mode, have to find out why. Should be an easy fix.
# raise nameError('HiThere')

# the sole argument to raise indicates the exception to be raised. This must be either an exception instance or an exception class (a class that derives from Exception). If an exception class is passedl it will be implicitly instantiated by calling its constructor with no arguments:

# raise valueError # Shorthand for 'raise ValueError()'

# If you need to determine whether an exception was raised but don't intend to handle it, a simpler form of the raise statement allows you to re-raise the exception:

try:
	raise NameError('HiThere')
except NameError:
	print('An exception flew by!')
	raise
