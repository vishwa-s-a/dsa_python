
def binary_search(arr,n,low,high):
    if(low>high):
        return False
    mid=(low+high)//2
    if(arr[mid]==n):
        return True
    elif(arr[mid]>n):
        return binary_search(arr,n,low,mid-1)
    else:
        return binary_search(arr,n,mid+1,high)

arr=[3,4,5,6,9,14,15,34,56]
high=len(arr)-1
print(binary_search(arr,14,0,high))