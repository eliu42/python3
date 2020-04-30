# Returns the index of the first item whose value is equal to x. raises a ValueError if there is no such item.
#list.index(x,[start[,end]]), where end is non inclusive

l = [0, 1, 2, 3, 4, 1]

print(l.index(1))
print(l.index(1, 2))
print(l.index(1, 2, 3))
