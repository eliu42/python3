a = [-1, 1, 66.25, 333, 333, 1234.5]
b = a
del a[0]
print(a)
del a[2:4]
print(a)
del a[:]
print(a)

# Deleting entire statements is also possible, but it free the memory and changes it to null?
print(b)
del b[:]
print(b)
