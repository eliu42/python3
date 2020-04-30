t = 12345, 54321, "hello!"
print(t[0])
print(t)
# tuples may be nested:
u = t, (1, 2, 3, 4, 5)
print(u)
# Tuples are immutable.
# The follow will produce an error:

# t[0] = 88888

# However, tuples contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
v[0][0] = 4
print(v)

# It seems tuples can be reassigned, but not modified?
empty = ()
singleton = "hello",
double = "world",
print(len(empty))
print(len(singleton))
print(singleton)
empty = singleton, double
print(empty)
x, y = empty
print(x)
print(y)
