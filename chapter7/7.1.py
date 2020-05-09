# 7.1 Fancier Output Formatting

# To use formatted string literals, begina  string with f or F befpre the opening qutation mark or triple qutation mark. Inside this string, you can write a Python expression between { and } characters that can refer to variables or literal values.

year = 2016
event = 'Referendum'
print(f'Results of the {year} {event}')

# The str.format() method of strings requres more manual effort. You'll still use { and } to mark where a varaible will be substituted and can provide detaileed formatting directives, but you'll also need to provide the information to be formatted.
# This is similar to the printf function

yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
print('{:-9} YES votes {:2.2%}'.format(yes_votes, percentage))

# When you don't need facny output but just want a quick display of some variables for debugging purposes, you can covert any value to a string with the repr() or str() functions.

# The str() function is meant to return representations of values which are failry human-readablw, while repr() is meant to generate representations which can be read by the interpreter (or will force a SyntaxError if there is no equivalent syntax). For objects which don't have a particular representation for human consumption, str() will return the same value as repr(). Many values, such as numbers or structures like lists and dictionaries, have the same representation using either function. Strings, in particular, have two distrinct representations.

# Some examples:

s = 'hello, world.'
print('----------')
print(s)
print(str(s))
print(repr(s))
print(str(1/7))
x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)
# The repr() of string adds string quotes and backslashes:
hello = 'hello, world\n'
hellos = repr(hello) 
print(hello)
print(hellos)
# The argument to repr() may be any Python object:
repr((x, y, ('spam', 'eggs')))

