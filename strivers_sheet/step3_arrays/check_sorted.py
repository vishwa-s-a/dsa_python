# to check whether the given array is sorted in ascending order or not

def check_sorted(arr,n):
    if(n==1):
        return True
    for i in range(1,n,1):
        if (arr[i-1]>arr[i]):
            return False
    return True
l1=[1,2,0,3,4,5]
print(check_sorted(l1,len(l1)))