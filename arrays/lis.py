#this is longest increasing subsequence
arr=input("Enter the numbers:\n").split(" ")
n=len(arr)
max=0
result=[1 for i in range(n)]
for i in range(1,n,1):
    for j in range(0,i,1):
        if(arr[i]>arr[j] and result[i]<result[j]+1):
            result[i]=result[j]+1
for i in result:
    if(max<i):
        max=i
print(max)