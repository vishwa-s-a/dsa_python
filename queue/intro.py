#should use deque of collections module for queue
# can also use list, an example is explained below
queue=list()
queue.insert(0,'vishwa')
queue.insert(0,'sachin')
queue.insert(0,'soumya')
print(queue.pop())
print(queue)



#now using deque
from collections import deque
q1=deque()
q1.append(1)
q1.append(2)
print(q1.popleft())

q2=deque()
q2.appendleft(1)
q2.appendleft(2)
print(q2.pop())
