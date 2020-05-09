# Basic usage of the str.format() method looks like this:

print('We are the {} who say "{}!"'.format('knights', 'Ni'))

# The brackets and characters within them (called format fields) are replaced with the objects passed into the str.format() method. A number in the brackets can be used to refer to the position of the object passed into the str.format() method. 

print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))

# If keyword arugments are used in the str.format() method, their values are referred to by using the name of the argument.

print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))

# Positional and keyword arguments can be arbitrarily combined:
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
						   other='Georg'))
# If you have a really long format string that you don't want to spoilt up, it would be nice if you could reference the varaibles to be formatted by name instead of by position. This can be done by simply passing the dict and using square brackets '[]' to access the keys

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}, Sjoerd: {0[Sjoerd]:d}; '
      'Dcab: {0[Dcab]:d}'.format(table))

# This could also be done by passing the table as keyword arguments with the '**' notation.

# table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
# print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Dcab: {0[Dcab]:d}'.format(table))

# this is particularly useful in combination with the built-in funcction vars(), which returns a dictionary containing all local variables.

# As an example, the following lines produce a tidily-aligned set of columns giving integers and their squares and cubes:

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
