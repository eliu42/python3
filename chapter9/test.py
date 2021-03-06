class Reverse:
	"""Iterator for looping over a sequence backwards."""
	def __init__(self, data):
		self.data = data
		self. index = len(data)

	def _iter_(self):
		return self

	def _next_(self):
		if self.index == 0:
			raise StopIteration
		self.index = self.index - 1
		return self.data[self.index]

rev = Reverse('spam')
print(iter(rev))
for char in rev:
	print(char)
