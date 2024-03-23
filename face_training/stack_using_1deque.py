from collections import deque
class Stack:
    def __init__(self):
        self.q=deque()
    
    def push(self,x):
        n=len(self.q)

        self.q.append(x)

        for i in range(n):
            self.q.append(self.q.popleft())
    
    def top(self):
        if self.q:
            return self.q[0]
        return None
    
    def pop(self):
        if self.q:
            return self.q.popleft()
        return None

    def length(self):
        return len(self.q)
    
if __name__ == '__main__':
    st = Stack()
    st.push(1)
    st.push(2)
    st.push(3)
    print(st.pop())
    print(st.top())