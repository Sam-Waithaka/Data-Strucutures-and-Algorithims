'''
Would use a list in python but that would be inefficient as removing
the first item on the list would require big O of linear time complexity
as all subsequent items would require being shifted down in their positions
'''
from collections import deque

queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)
queue.append(6)

print(queue)

x = queue.popleft()
print(queue)
y = queue.pop()
print(queue)