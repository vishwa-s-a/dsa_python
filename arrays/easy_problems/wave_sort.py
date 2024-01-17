# we have to sort the array in wave fashion
arr=[10, 90, 49, 2, 1, 5, 23]
# expected output: 20,8,10,4,6,2
arr.sort()
print(arr)
i=0
j=len(arr)-1
new_arr=list()
while(i<j):
    new_arr.append(arr[j])
    new_arr.append(arr[i])
    i+=1
    j-=1
print(new_arr)
