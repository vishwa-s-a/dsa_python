import collections

queue=collections.deque()
queue.appendleft('1')
head=-1
for i in range(5):
    queue.appendleft(queue[head]+'0')
    queue.appendleft(queue[head]+'1')
    head-=1
print(queue)