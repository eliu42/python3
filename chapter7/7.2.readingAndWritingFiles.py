# The function open() returns a file object, and is most commonly used with two arugments: open(filename, mode).
f = open('workfile', 'w')

# When 'b' appended is appended to the mode, it opens the file in binary mode: now the data is read and written in the form of bytes objects. This mode should be used for all files that don't contain text.

# It is good practice to use the 'with' keyword when dealing with file objects. The advantage is that the file is properly closed after its suite finishes, even if an exception is raised at some point. Using with is also much shorter than writing equivalent try-finally blocks:

with open('workfile') as f:
	read_data = f.read()

# We can check that the file has been automatically closed.
print(f.closed)

# If you're not using the with keyword, then you should call f.close() to close the file and immediately free up any system resources used by it. If you don't explicitly close a file, Python's garbage collector will eventually destroy the object and close the open file for you, but the file may stay open for a while. Another risk is that different Python Implementations will do this clean-up at different times.

# After a file object is closed, either by a with statement or by calling f.close() attempts to use the file object will automatically fail.

f.close()
f.read()
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#ValueError: I/O operation on closed file.

