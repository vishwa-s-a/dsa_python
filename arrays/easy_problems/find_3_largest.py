import sys
def find_3_largest(arr):
    n=len(arr)
    if(n<3):
        print("Entered array is invalid")
        return 
    first=second=third=-sys.maxsize
    for i in range(0,n):
        if(arr[i]>first):
            third=second
            second=first
            first=arr[i]
        elif(arr[i]>second):
            third=second
            second=arr[i]
        elif(arr[i]>third):
            third=arr[i]
    print('The three largest numbers in the array: ',first,second,third)
# print(sys.maxsize)
raw_input=input("Enter the array elements: ")
proc_input=raw_input.split(',')
for i in range(0,len(proc_input)):
    proc_input[i]=int(proc_input[i])
find_3_largest(proc_input)

