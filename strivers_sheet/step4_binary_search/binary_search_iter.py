
def binary_search(arr,n):
    low=0
    high=len(arr)-1
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]==n):
            return True
        elif(arr[mid]>n):
            high=mid-1
        else:
            low=mid+1
    return False


arr=[3,4,5,6,9,14,15,34,56]
print(binary_search(arr,99))