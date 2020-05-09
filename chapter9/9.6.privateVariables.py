# 9.6 Private Variables
# "Private" instance variables that cannot be accessed except from inside an objec don't exist in Python. However, there is a convention that is followed by most Python code: a name pre fixed with an underscore (e.g. _spam) should be treated as a non-public part of the API (whether it is a function, a method or a data member). It should be considered an implementation detail and subject to change without notice.
#
#
class Mapping:
	def _init_(self, iterable):
		self.item_list = []
		self._update(iterable)

	def update(self, iterable):
		for item in iterable:
			self.items_list.append(item)

	_update = update

class MappingSubClass(Mapping):

	def update(self, keys, values):
		# Provides new signatures for update()
		# Does not break _init_()
		for item in zip(keys, values):
			self.items_list.append(item)

a = Mapping()
b = MappingSubClass()

print(a)
print(b)

#
#
#
