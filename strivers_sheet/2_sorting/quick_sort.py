'''
it uses the divide and conquer approach to solve the problem
here the time complexity is O(nlogn)
space complexity is O(1) as it does not use any extra array space but uses stack space

* thats why its slightly better than merge sort

worst case time complexity is O(n^2) if we end up choosing the smallest or the largest element as pivot always

'''
def partition(arr,low,high):
    pivot=arr[low]# by default we are taking the first element as the pivot
    i=low
    j=high
    while(j>=i):
        if(arr[i]<=pivot):
            i+=1
        if(arr[j]>=pivot):
            j-=1
        if(j>=i and (arr[i]>pivot and arr[j]<pivot)):
            arr[i],arr[j]=arr[j],arr[i]
    arr[low],arr[j]=arr[j],arr[low]
    return j

def quick_sort(arr,low,high):
    if(low >= high):
        return
    correct_index=partition(arr,low,high)
    quick_sort(arr,low,correct_index-1)
    quick_sort(arr,correct_index+1,high)

l1=input('Enter the array: ').split(",")
l=[eval(i) for i in l1]
quick_sort(l,0,len(l)-1)
print(l)