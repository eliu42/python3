# The rest of the examples in this section will assume that a file object called f has already been created.

# To read a file's contents, call f.read(size), which reads some quantity of data and returns it as a string (in text mode) or bytes object(in binary mode). 'size' is an optional numeric argument. When size is omitted or negative, the entire contents of the file will be read and returned; it's your problem if the file is twice as large as your machine's memory. Otherwise, at most 'size' characters (in text mode) or size bytes (in binary mode) are read and retruned. If the end of the file has been reached, f.read() will return an empty string('').

with open('newfile') as f:
	print(f.readline())
	print(f.readline())

with open('newlinefile') as f:
	print(f.readline())
	print(f.readline())
	print(f.readline())
	
with open('newlinefile') as f:
	for line in f:
		print(line, end="")

# If you want to read all the lines of a file in a list you can also use list(f) or f.readlines(). f.write(string) writes the contents of 'string' to the file, returning the number of charcters written.

with open('test', 'a') as f:
	f.write('This is a test\n')

# Other types of obhects need to be converted - either to a string (in text mode) or a bytes object (in binary mode) - before writing them:

value = ('the answer', 42)
s = str(value)
print(s)
with open('theAnswer', 'w') as f:
	print(f.write(s))

# The function f.tell() returns an integer giving the file object's curent position in the file represented as number of bytes from the beginning of the file when i nbinary mode and an opaque number when in text mode.

# To change the file object's position, use f.seek(offset, whence). The position is computed from adding offset to a reference point; the reference point is selected by the 'whence' argument. A 'whence' value of 0 measures from the beginning of the file, 1 uses the current file position, and 2 uses the end of the file as the reference point. whence can be omitted and defaults to 0, using the beginning of the file as the reference point.

f = open('workfile', 'rb+')
f.write(b'0123456789abcdef')

print(f.seek(5)) # Go to the 6th bye in the file

print(f.read(1))

print(f.seek(-3, 2)) # Go to the 3rdd byte before the end

print(f.read(1))

# In text files (those opened without a 'b' in the mode string), only seeks relative to the beginning of the file are allowed (the exception being seeking to the very file end with seek(0,2)) and the only valid offset values are those returned from the f.tell(), or zero. Any other offset value produces undefined behavior.

# File objects have some additional methods, such as isatty() and truncate() which are less frequently used; consult the Library Reference for a complete guide to file objects.
