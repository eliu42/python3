# list.append(x) is meant to add on a single item to a list. To extend all items from an iterable, use list.extend
# What other data types can we test using this? We don't know yet.


lst = [1, 2, 3]
toAppend = [5, 6]

lst.append(4)
print(lst)
lst.append(toAppend)
print(lst)
lst[len(lst):] = toAppend
print(lst)
