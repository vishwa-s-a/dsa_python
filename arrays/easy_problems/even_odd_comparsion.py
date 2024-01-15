# here we will have array elements in such way we can find that even indexed elements are greater than the odd indexed elements

#imp considerations is that we are taking the starting index of the array as '1'
def even_odd_segregations(arr):
    arr.sort()
    p=0
    q=len(arr)-1
    new_arr=list()#this list will contain our final answer
    #print(len(new_arr))#we will get 0 as  len as above line will make a empty list with len=0
    #other approach to create a new array or list is
    #new_arr=[0]*len(arr)
    for i in range(0,len(arr)):
        #this is for identification of even indices
        if((i+1)%2==0):
            new_arr.append(arr[q])
            q-=1
        else:
            new_arr.append(arr[p])
            p+=1
    for i in new_arr:
        print(i,end=', ')
    print('\r')
arr_str=input('Enter the array: ')
split_arr=arr_str.split(',')
real_arr=list()#we have to declare if not we get the error as real_error not defined
for i in range(0,len(split_arr)):
    real_arr.append(int(split_arr[i]))
even_odd_segregations(real_arr)