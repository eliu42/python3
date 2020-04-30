tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
print(tel['jack'])
del tel['sape']
tel['irv'] = 4127
print(tel)
print(list(tel))
print(sorted(tel))

d = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(d)

# In addition, dict comprehensions can be used to create dictionaries from arbitrary key and value expressions:

print({x: x**2 for x in (2, 4, 6)})

# When the keys are simple strings, it is sometimes easier to specify pairs using keyword arguemtns:

print(dict(one=1, two=2, three=3))
