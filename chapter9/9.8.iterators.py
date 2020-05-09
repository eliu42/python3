# 9.8 Iterators

# By now you have probably noticed that most container objects can be looped over using a for statement:

for element in [1, 2, 3]:
	print(element)
for element in (1, 2, 3):
	print(element)
for key in {'one':1, 'two':2}:
	print(key)
for char in "123":
	print(char)
for line in open("myfile.txt"):
	print(line, end='')

# This style of access is clear, concise, and convenient. The use iterators pervades and unifies Python. Behind the senes, the for statement calls iter() on the container object. The function returns an iterator object that defines method _next_() which accesses elements in the container one at a time. When there are no more elements, _next_(() raises a StopIteration exception which tells the for loop to terminate. You can call the _next_() method using the next() builtin-in function; this example shows how it all works:

s = 'abc'
it = iter(s)
print(it)
print(next(it))
print(next(it))
print(next(it))
	
# Having seen the mechanics behind the iterator protocol, it is easy to add iterator behavior to your classes. Define an _iter_() method which retuns an object with a _next_() method. If the class defines _next_(), then _iter_() can just return self:

class Reverse:
	"""Iterator for looping over a sequence backwards."""
	def __init__(self, data):
		self.data = data
		self.index = len(data)

	def __iter__(self):
		return self

	def __next__(self):
		if self.index == 0:
			raise StopIteration
		self.index = self.index - 1
		return self.data[self.index]

rev = Reverse('spam')
print(iter(rev))
for char in rev:
	print(char)
