import time
import multiprocessing

def square(arr,q):
    for idx, i in enumerate(arr):
        print(f"Square of {i} is : {i*i}")
        q.put(i*i)

arr=[1,2,3,4,5]
if __name__=='__main__':
    q=multiprocessing.Queue()
    p1=multiprocessing.Process(target=square,args=(arr,q))

    p1.start()
    p1.join()

    while (q.empty() is False):
        print(q.get())
    