def bubble_sort_recursive(arr,n):
    if(n==0):
        return 
    for i in range(0,n,1):
        if(arr[i]>arr[i+1]):
            arr[i],arr[i+1]=arr[i+1],arr[i]
    print(arr)
    bubble_sort_recursive(arr,n-1)

l1=input('Enter the array: ').split(",")
l=[eval(i) for i in l1]
bubble_sort_recursive(l,len(l)-1)
print(l)