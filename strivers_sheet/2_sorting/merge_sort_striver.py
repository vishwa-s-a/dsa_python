'''
this code is from strivers notes and guide on merge sort

time complexity is O(n* logn) here the log is base 2
space complexity is O(n)
'''

def merge(arr,start,mid,end):
    ans=[] #temp list to store the resulting merged array

    #left and right pointers point to the starting point of the 2 divided array
    left=start
    right=mid+1
    while(left<=mid and right<=end):
        if(arr[left]<=arr[right]):
            ans.append(arr[left])
            left+=1
        else:
            ans.append(arr[right])
            right+=1
    while(left<=mid):
        ans.append(arr[left])
        left+=1
    while(right<=end):
        ans.append(arr[right])
        right+=1
    
    # now we have the sorted and merged array in ans. we got to shift this temp array to our original array arr
    for i in range(start,end+1,1):
        arr[i]=ans[i-start]
def merge_sort(arr,start,end):
    if(start!=end):
        mid=(start+end)//2
        merge_sort(arr,start,mid)
        merge_sort(arr,mid+1,end)
        merge(arr,start,mid,end)
        
l1=input('Enter the array: ').split(",")
l=[eval(i) for i in l1]
n=len(l)
merge_sort(l,0,n-1)
print(l)