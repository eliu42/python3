# 5.1.2 Using Lists as Queues
#It is also possible to use a list as a queue, where the firt element added is the first element retrieved ("first-in, "first-out"); however, lists are not efficient for this purpose. While appends and appends from the end of list are fast, doing inserts or pops from the beginning of a list is slow (because all of the other elements have to be shifted by one).
# To implement a queue, use colletions.dequeu which was designed to have fast appends and pops from both ends. For example:


from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
print(queue.popleft())
print(queue.popleft())
print(queue)

# How is this implemented in code?
