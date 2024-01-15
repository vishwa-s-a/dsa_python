arr=[1,2,3,4,5]
print('the subarrays of this array are: ')
def sub_array(arr):
    for i in range(0,len(arr)):
        for j in range(i,len(arr)):
            for k in range(i,j+1):
                print(arr[k],end=" ")
            print('\r')
sub_array(arr)