'''
implementing stack using 2 queues(here it is my own way of using list instead of queue)
'''
class stack:
    def __init__(self):
        self.q1=[]
        self.q2=[]
    def push(self,x):
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.pop(0))
        self.q1,self.q2=self.q2,self.q1
    def pop(self):
        if not self.q1:
            return None
        return self.q1.pop(0)
    def top(self):
        if not self.q1:
            return -1
        return self.q1[0]
    def size(self):
        return len(self.q1)
    
s=stack()
s.push(1)
s.push(2)
s.push(3)
print(s.top())

        