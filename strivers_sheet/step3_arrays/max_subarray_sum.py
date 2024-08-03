#kadanes algorithm to find out the maximum subarray sum

import sys
def maxSubarraySum(arr,n):
    maxi=-sys.maxsize-1
    sum=0
    pointer=0
    start,end=-1,-1
    for i in range(n):
        if(sum==0):
            pointer=i
        sum+=arr[i]
        if(sum>maxi):
            maxi=sum
            start=pointer
            end=i
        if(sum<0):
            sum=0
    print('The start and end of the subarray is: ',start,end)
    return maxi

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
n = len(arr)
maxSum = maxSubarraySum(arr, n)
print("The maximum subarray sum is:", maxSum)