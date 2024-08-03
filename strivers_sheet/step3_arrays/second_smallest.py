#to find the second smallest and largest element

# below function1 uses 2 for loops to do the job
def function1(arr,n):
    if(n==0 or n==1):
        print('-1,-1')
        return
    smallest=float('inf') # inf represents the positive infinity
    second_smallest=float('inf')
    largest=float('-inf')
    second_largest=float('-inf')
    for i in range(0,n):
        smallest=min(smallest,arr[i])
        largest=max(largest,arr[i])
    for i in range(0,n):
        if(arr[i]<second_smallest and arr[i]!=smallest):
            second_smallest=arr[i]
        if(arr[i]>second_largest and arr[i]!=largest):
            second_largest=arr[i]
    print(second_smallest,second_largest)


# below function2 uses 1 for loop to do the job
def function2(arr,n):
    if(n==0 or n==1):
        print('-1,-1')
        return
    smallest=float('inf')
    second_smallest=float('inf')
    largest=float('-inf')
    second_largest=float('-inf')
    for i in range(0,n):
        if(arr[i]<smallest):
            second_smallest=smallest
            smallest=arr[i]
        elif(arr[i]<second_smallest and arr[i]!=smallest):
            second_smallest=arr[i]
        
        if(arr[i]>largest):
            second_largest=largest
            largest=arr[i]
        elif(arr[i]>second_largest and arr[i]!=largest):
            second_largest=arr[i]
    print(second_smallest,second_largest)    
l1=[1,2,4,6,7,5]
function1(l1,len(l1))
function2(l1,len(l1))