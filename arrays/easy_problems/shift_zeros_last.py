def shift_zeros_end(arr):
    n=len(arr)
    count=0
    #this for loop shifts all non zero elements to start of the array
    for i in range(0,n):
        if(arr[i]!=0):
            arr[count]=arr[i]
            count+=1
    # use while loop to fill all remaining positions with 0
    while(count<n):
        arr[count]=0
        count+=1
    for i in arr:
        print(i,end=', ')
    print('\r')
arr=[1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
print('The resulting array is : ')
shift_zeros_end(arr)