#this is longest increasing subsequence
arr=input("Enter the numbers:\n").split(" ")
n=len(arr)
answer=0
res1=[1 for i in range(n)]
res2=[1 for i in range(n)]
for i in range(1,n,1):
    for j in range(0,i,1):
        if(arr[i]>arr[j] and res1[i]<res1[j]+1):
            res1[i]=res1[j]+1
for i in range(n-2,-1,-1):
    for j in range(n-1,-1,-1):
        if(arr[i]>arr[j] and res2[i]<res2[j]+1):
            res2[i]=res2[j]+1
for i in range(n):
    answer=max(answer,res1[i]+res2[i]-1)
    
print(answer)