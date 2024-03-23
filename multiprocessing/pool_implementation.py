'''
implementing map and reduce method using pool in python 
'''

import time
from multiprocessing import Pool

def f(n):
    sum=0
    for x in range(1000):
        sum+=x*x
    return sum

t1=time.time()
p=Pool()
result=p.map(f,range(100000))
p.close()
p.join()

print('Pool took: ',time.time()-t1)

t2=time.time()
result=[]
for x in range(100000):
    result.append(f(x))

print('Serial processing took: ',time.time()-t2)