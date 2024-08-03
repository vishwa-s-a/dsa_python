#in given array we have to find the sub-array whose sum is equal to given k 

def sum_subarray(arr,k):
    d={}
    sum=0
    max_len=0
    for i in range(len(arr)):
        sum+=arr[i]
        if(sum==k):
           max_len=i+1
        if(sum not in d):# this we mainly do to capture only the first occurence of that sum
           d[sum]=i
        print(d)
        if(sum-k in d):
           max_len=max(max_len,i-d[sum-k])
    print(max_len)
l=[-13,0,6,15,16,2,15,-12,17,-16,0,-3,19,-3,2,-9,-6]
k=17
sum_subarray(l,k) 