print(list(range(3, 6)))
args = [3, 6]
print(list(range(*args)))

#In the same fashion, dictionaries can deliver keyword arguments with the **-operator.

def parrot(voltage, state="a stiff", action="voom"):
	print("-- This parrot wouldn't", action, ' ')
	print("if you put", voltage, "volts through it.", ' ')
	print("E's", state, '!')

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)

