# It is possible to write programs that handle selected exceptions. Look at the following example, which asks the user for input until a valid integer has been entered, but allows the uesr to interrupt the program (using Control-C or whatever the operating system supports); note that a user-generated interruption is signalled by raising the KeyboardInterrupt exception.

while True:
	try:
		x = int(input("Please enter a number: "))
		break
	except ValueError:
		print("Oops! That was no valid number. Try again...")

# 	The try statement works as follows.
#	First, the try clause (the statement(s) between the try and except keywords) is executed.
#	If no exception occurs, the except clause is skipped and execution of the try statement is finished.
#	If an exception occurs during execution of the try clause, the rest of the clause is skipped. Then if its type matches the exception named after the except keyword, the except clause is executed, and then execution continues after the try statement.
#	If an exception occurs which does not match the exception named in the except clause, is it passed on to out try statements; if no handler is found, is it an unhandled exception and exeuction stops with a message as shown above.

# A try statement may have more than one except clause, to specify handlers for different exceptions. At most one handler will be executed. Handlers only handle exceptions that occur in the corresponding try clause, not in other handlers of the same try statement. An except clause may name multiple exceptions as a parenthesized tuple, for example:

#except (RuntimeError, TypeError, NameError):
#	pass

# A Class is an except clause is compatible with an exception if it is the same class or a base class thereof (but not the other way around — an except clause listing a derived class is not compatible with a base class). For example, the following code will print B, C, D in that order:

class B(Exception):
	pass

class E(B):
	pass

class D(E):
	pass

for cls in [B, E, D]:
	try:
		raise cls()
	except D:
		print("D")
	except E:
		print("E")
	except B:
		print("B")

# Note that if the except clauses were reversed (with except B first), it would have printed B, B, B — the first matching except clause is triggered.

# The last except clause may omit the exception name(s), to serve as a wildcard. Use this with extreme caution, since it is easy to mask a real programming error in this way! It can also be used to print an error message and then re-raise the exception (allowing a caller to handle the exception as well):
import sys

try:
	f = open('myfile.txt')
	s = f.readline()
	i = int(s.strip())
except OSError as err:
	print("OS error: {0}".format(err))
except ValueError:
	print("Could not convert data to an integer.")
except:
	print("Unexpected error:", sys. exc_info()[0])
	raise

# The try ... except statement has an optional else clause, which, when present, must follow all except clauses. It is useful for code that must be executed if the try clause does not raise an exception. For example:

for arg in sys.argv[0]:
	try:
		f = open (arg, 'r')
	except OSError:
		print('cannot open', arg)
	else:
		print(arg, 'has', ken(f.readlines()), 'lines')
		f.close()

# The use of the else clause is better than adding additional code to the try clause because it avoids accidentally catching an exception that wasn't raised by the code being protected by the try ... except statement.

# When an exception occurs, it may have an associated value, also known as the exception's argument. The presence and type of the argument depend of the exception type.

# The except clause may specify a variable after the exception name. The variable is bound to an exception instance with the arguments stored in instance.args. For convenience, the exception instance defines __str__() so the arguments can be printed directly without having to reference .args. One may also instantiate an exception first before raising it and add any attributes to it as desired.

try:
	raise Exception('spam', 'eggs')
except Exception as inst:
	print(type(inst))	# The exception intance.
	print(inst.args)	# Arguments stored in .args.
	print(inst)		# __str__ allows args to be printed directly, but may be overridden in exceptino subclasses
	x, y = inst.args	# Unpack args
	print('x =', x)
	print('y =', y)

# If an exception has arguments, they are printed as the last part ('detail') of the message for unhandled exceptions.
# Exception handlers don't just handle exceptions if they occyr immediately in the try clause, but also if they occur inside functions that are called (even indirectly) in the try clause. For example:

def this_fails():
	x = 1/0

try:
	this_fails()
except ZeroDivisionError as err:
	print('Handling run-time error:', err
