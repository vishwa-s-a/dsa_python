'''
here it selects a element and places it in its correct order or place or index

time complexity is same as the other two sorting techniques
that is summation of n natural numbers 
O(n^2) this is the average and the worst case scenarios

O(n) is the best case where there are no swaps, only when the given array is already sorted

'''
l1=input('enter the array: ').split(",")
l=[eval(i) for i in l1]
for i in range(1,len(l),1):

    # this following code is written by me and not well optimized so ignore it
    # for j in range(i,0,-1):
    #     if(l[j]<l[j-1]):
    #         l[j],l[j-1]=l[j-1],l[j]
    #         print('Inner if')
    #     print('inner for loop')

    # this part of code is inspired from striver which is more optimized and runs less number of 
    # of while loop which can be seen in the bottom section
    j=i
    while(j>0 and l[j]<l[j-1]):
        l[j],l[j-1]=l[j-1],l[j]
        print('Inner while loop')
        j-=1
print(l)