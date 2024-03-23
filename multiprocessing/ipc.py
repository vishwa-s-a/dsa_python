import time
import multiprocessing

result=[]
def square(arr,mem,val):
    global result
    for idx, i in enumerate(arr):
        print(f"Square of {i} is : {i*i}")
        result.append(i*i)
        mem[idx]=i*i
        val.value+=i*i
        time.sleep(1)
    print('Inside the process, result: ',result)

arr=[1,2,3,4,5]
if __name__=='__main__':
    shared_mem=multiprocessing.Array('i',5)
    shared_val=multiprocessing.Value('d',0.0)# here d refers double and the value is initialised to 0.0
    p1=multiprocessing.Process(target=square,args=(arr,shared_mem,shared_val))
    p1.start()
    p1.join()
    print('Outside the process, result: ',result)
    print('The shared memory array is : ')
    for i in range(5):
        print(shared_mem[i],end=' ')
    print('\r')
    print('The shared value variable(contains the sum of all variables) is : ',shared_val.value)