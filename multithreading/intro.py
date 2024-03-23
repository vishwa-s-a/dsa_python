import time
import threading

'''
* each process has its own virtual memory or space and each process can have as many threads required
  then each thread can access the memory assigned to that particular process

* in multiprocessing each process has its own memory and ipc can take place between process using i) files ii) shared memory iii) message pipe

'''


def square(arr):
    print('The square of the numbers: ')
    for i in arr:
        time.sleep(0.2)
        print('square: ',i*i)


def cube(arr):
    print('The cube of the numbers: ')
    for i in arr:
        time.sleep(0.2)
        print('cube: ',i*i*i)

arr=[2,5,7,9]
def with_out_multithreading():
    t=time.time()
    square(arr)
    cube(arr)
    print('Time taken without multithreading is: ',time.time()-t)

with_out_multithreading()
print('\n')

def with_multithreading():
    t=time.time()
    t1=threading.Thread(target=square,args=(arr,))
    t2=threading.Thread(target=cube,args=(arr,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('Time taken after using multi threading: ',time.time()-t)

with_multithreading()