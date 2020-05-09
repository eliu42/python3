# 8.6 Defining Clean-up Actions

# The try statement has another optinal clause which is intended to define clean-up actions that must be eecuted under all circumstances. For example:

#try:
#	raise KeyboardInterrupt
#finally:
#	print('Goodbye, world!')

# If a finally clause is present, the finally clause will execute as the last task before the try statement completes. The finally clause runs whether or not the try statement produces an exception. the follow points discuss more complex cases when an exception occurs:


	# If an exception occurs during execution of the try clause, the exeception may be handed by an except clause. If the exception is not handled by an except clause, the exception is re-raised after the finally clause has been exeucuted.
	# An exception could occur during execution  of an except or else clause. Again, the exception
	# If the try statement reaches a break, continue, or return statement, the finally clause will execute just prior to the break, continue or return statement's execution.
	# If a finally clause includes a return statement, the returned value will be the one from the finally clause's return statement, not the value from the try clause's return statement.

# For example:

def bool_return():
	try:
		return True
	finally:
		return False

print(bool_return())

def divide(x, y):
	try:
		result = x / y
	except ZeroDivisionError:
		print("division by zero!")
	else:
		print("result is", result)
	finally:
		print("executing finally clause")

divide(1, 2)
divide('2', '1')

# As you can see, the finally clause is executed in any event. The TypeError raised by divided two strings is not handled by the except clause and therefore re-raised after the finally clause has been executed. Reraises are built in raise error statementes.

# In real world applications, the finally clause is useful for releasing external resources (such as files or network connections) regardless of whether the use of the resource was successful.
