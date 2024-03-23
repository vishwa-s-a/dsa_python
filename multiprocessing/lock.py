#using lock is essential when we are using shared resources and put the critical section code within
# the lock

import time
import multiprocessing

def deposit(val,lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        val.value=val.value+1
        lock.release()

def withdraw(val,lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        val.value=val.value-1
        lock.release()

lock=multiprocessing.Lock()
value=multiprocessing.Value('i',200)# this is the shared value
d=multiprocessing.Process(target=deposit,args=(value,lock))
w=multiprocessing.Process(target=withdraw,args=(value,lock))
d.start()
w.start()

d.join()
w.join()

print('Final value is: ',value.value)