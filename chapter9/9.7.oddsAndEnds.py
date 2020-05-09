# 9.7 Odds and Ends

#sometimes it is useful to have a data type similar to the Pascal "record" or C "struct", bundling together a new named data items. An empty class defintition will do nicely:

class Employee:
	pass

john = Employee()	# Create an empty employee record


# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000

# A piece of Python code that expects a particular abstract data type can often be passed a class that emulates the methods of that data type instead. For instance, if you have a function that formats some data from a file object, you can define a class with methods read() and readline() that get the data from a string buffer instead, and pass it as an argument.

# Instance method objects have attributes, too: m._self_ is the instance object with the method m(), and m._func_ is the function object corresponding to the method.
