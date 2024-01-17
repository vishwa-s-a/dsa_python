# cyclic sort has time complexity as O(n) and used to sort 1 to n values
# it is fixed that we will have a array 1,2,...,n
def cyclic_sort(arr,n):
    i=0
    while(i<n):
        correct_index=arr[i]-1
        if(arr[correct_index]!=arr[i]):
            swap(arr,correct_index,i)
        else:
            i+=1
            
def swap(arr,first,second):
    temp=arr[first]
    arr[first]=arr[second]
    arr[second]=temp

arr=[3, 2, 5, 6, 1, 4]
n=len(arr)
cyclic_sort(arr,n)
# we are directly passing the array so the function will modify this array itself
for i in arr:
    print(i,end=' ')
print('\r')