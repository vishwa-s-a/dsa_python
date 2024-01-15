import array

# we are trying to explore the arrays in python and its similarities with the list
arr=array.array("i",[1,2,3])
print("The elements in the array are: ",end="")
for i in range(0,3):
    print(arr[i],end=" ")
print("\r")

arr.append(5)
print("elements are appending: ",end="")
for i in arr:
    print(i,end=" ")
print("\r")

arr.insert(3,4)
print("Array after inserting the element: ",end="")
for i in arr:
    print(i,end=" ")
print("\r")

print("The popped element is : ",arr.pop())

for i in arr:
    print(i,end=" ")
print("\r")

# it doesn't return anything
arr.remove(1)

for i in arr:
    print(i,end=" ")
print("\r")

arr.append(1)

print("The index of 1 is ",arr.index(1))

print("Reversing the array")
arr.reverse()
for i in arr:
    print(i,end=" ")
print("\r")

print(arr.typecode)#gives the data type of the elements of the array has been initialized
print(arr.itemsize)#gives the size of the element in bytes

print("The buffer info of the array is : ")
print(arr.buffer_info())

print("count of 2 is : ",arr.count(2))

#extend method 

ar1=[1,2,3,4] # this is directly a list 
ar2=['a','b','c'] # this is also a list not a array
ar1.extend(ar2)
print(ar1)

# to convert the array into list
arr3=array.array('i',[66,67,68,69])

print(arr3,type(arr3))
list3=arr3.tolist()
print(list3,type(list3))
list3.append(70)
print(list3)