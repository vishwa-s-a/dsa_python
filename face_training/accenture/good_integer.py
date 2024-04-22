'''
an integer (z) is said to be a good integer 
if z=x^3+y^3
'''
import math
def find_good_integer(arr:list):
    for i in arr:
        l=1
        h=math.floor(pow(i,1/3))
        while(l<h):
            temp=pow(l,3)+pow(h,3)
            if(temp==i):
                print(f"{i} is a good integer")
                break
            else:
                l+=1

arr=input().split(",")
for i in range(len(arr)):
    arr[i]=eval(arr[i])
# print(arr)
find_good_integer(arr)