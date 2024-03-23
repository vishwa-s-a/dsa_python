from collections import deque

'''
implementing stack using 2 dequeues
as insertion and deletion are easy in dequeues
'''
class Stack:
    def __init__(self):
        self.q1=deque()
        self.q2=deque()
    
    def push(self,x):
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        
        self.q1,self.q2=self.q2,self.q1
    
    def pop(self):
        if self.q1:
            return self.q1.popleft()
        return None
    
    def top(self):
        if self.q1:
            return self.q1[0]
        return None
    
if __name__=='__main__':
    s=Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.top())
    print(s.pop())
    print(s.top())