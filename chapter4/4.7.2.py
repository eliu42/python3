def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, ' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

parrot(1000)
print("\n")
parrot(voltage=1000)
print("\n")
parrot(voltage=100000, action='VOOOOOM')
print("\n")
parrot(action='VOOOOOOM', voltage=1000000)
print("\n")
parrot('a million' 'bereft of life')
print("\n")
parrot('a thousand', state='pushing up the daisies')

# The parrot function accepts one required argument (voltage) and three optional arguments (state, action, and type). There must be a required argument either by explicit or implicit passing, and the other ones can be both, with explicit argument passing done in the order they are taken in by. Keywords can be followed by positional keywords but keywords cannot follow positional arguments.


