'''
implementing queue using 2 stacks

'''
class Queue:
    def __init__(self):
        self.s1=[]
        self.s2=[]
    
    def enqueue(self,x):
        
        #move from s1 to s2
        while self.s1:
            self.s2.append(self.s1.pop())
        
        self.s1.append(x)

        while self.s2:
            self.s1.append(self.s2.pop())
    
    def dequeue(self):
        if self.s1:
            return self.s1.pop()
        return None

if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())