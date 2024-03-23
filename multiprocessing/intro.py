import time
import multiprocessing

# here important thing to be noted is that the variables are not between two processes until inter process
# communication is used or in place

'''
* each process has its own virtual memory or space and each process can have as many threads required
  then each thread can access the memory assigned to that particular process

* in multiprocessing each process has its own memory and ipc can take place between process using i) files ii) shared memory iii) message pipe

'''
l1=list() #list to collect the squares calculated in the square function
def square(arr):
    for i in arr:
        print(f"Square of {i} is : {i*i}")
        l1.append(i*i)
        time.sleep(1)

def cube(arr):
    for i in arr:
        print(f"Cube of {i} is {i*i*i}")
        time.sleep(1)

arr=[1,2,3,4,5]
p1=multiprocessing.Process(target=square,args=(arr,))
p2=multiprocessing.Process(target=cube,args=(arr,))

p1.start()
p2.start()

p1.join()
p2.join()

print(l1)# this will print a empty list as in multiprocessing the variables are not shared by the main
# process to other process