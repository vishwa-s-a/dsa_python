import collections
import threading
import time

queue=collections.deque()

def place_order(arr):
    for i in arr:
        print('Placing order of: ',i)
        queue.appendleft(i)
        time.sleep(0.5)

def serve_order():
    while(len(queue)!=0):
        print('Serving order of: ',queue.pop())
        time.sleep(2)

orders = ['pizza','samosa','pasta','biryani','burger']
t1=threading.Thread(target=place_order,args=(orders,))
t2=threading.Thread(target=serve_order,args=())

t1.start()
time.sleep(1)
t2.start()

t1.join()
t2.join()

