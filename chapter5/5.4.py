basket = {'apple', 'orange', 'apple', "pear", "orange", "banana"}
print(basket)
print("orange" in basket)
print("crabgrass" in basket)

# Demonstrate set operations on unique letters from two words

a = set("abracadabra")
b = set("alacazam")
print(a)
print(b)
print(a - b) # Letters in a but not in b
print(a | b)
print(a & b)
print(a ^ b)
