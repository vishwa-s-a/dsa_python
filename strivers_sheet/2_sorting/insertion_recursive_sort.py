
def insertion_recursive_sort(arr,n,i):
    if(i>n):
        return
    j=i # let it be as j equivalent to i, so we can track where our specific element moves
    while(j>0 and arr[j]<=arr[j-1]):
        arr[j],arr[j-1]=arr[j-1],arr[j]
        j-=1
    insertion_recursive_sort(arr,n,i+1)
l1=input('Enter the array: ').split(",")
l=[eval(i) for i in l1]
insertion_recursive_sort(l,len(l)-1,1)
print(l)