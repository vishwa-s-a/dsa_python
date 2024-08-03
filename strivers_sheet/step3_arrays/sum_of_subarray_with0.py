#in given array we have to find the sub-array whose sum is equal to given k 
# here the code is similar to the sum_of_subarray.py no changes so dont worry

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
        if(sum in d):
           max_len=max(max_len,i-d[sum])
    print(max_len)
l=[-1,1,-1,1]
k=0
sum_subarray(l,k) 