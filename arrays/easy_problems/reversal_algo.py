#we have to rotate the array as many time specified in the input using the reversal algo
def reverse_arr(arr,start,end):
    while(start<end):
        temp=arr[start]
        arr[start]=arr[end]
        arr[end]=temp
        start+=1
        end-=1
def rotate_arr(arr,t):
    t=t%len(arr)
    if(t==0):
        pass
    elif(t==len(arr)):
        arr.reverse()
    else:
        reverse_arr(arr,0,t-1)
        reverse_arr(arr,t,len(arr)-1)
        arr.reverse()
    print(arr)
arr_str=input('Enter the array: ')
split_arr=arr_str.split(',')
real_arr=list()#we have to declare if not we get the error as real_error not defined
for i in range(0,len(split_arr)):
    real_arr.append(int(split_arr[i]))
t=int(input("Enter the times of rotation: "))
rotate_arr(real_arr,t)