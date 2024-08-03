#we get a increasing order sorted array with duplicates

#using two pointer approach
def remove_duplicates(arr,n):
    i=0
    for j in range(1,n,1):
        if(arr[i]!=arr[j]):
            i+=1
            arr[i]=arr[j]
    return i+1
l1=[1,1,2,2,2,3,3,4,5]
ind=remove_duplicates(l1,len(l1))
for i in range(ind):
    print(l1[i],end=" ")
print("")