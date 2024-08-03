#selects the minimum and swaps it  and then moves forward, basically the minimum element is pushed to the beginning of array

'''
time complexity is o(n^2)
for best,worst and average case
'''

l1=input('enter the array ').split(",")
l=[eval(i) for i in l1]
for i in range(0,len(l)-1,1):
    minimum=i
    for j in range(i+1,len(l),1):
        if(l[j]<l[i]):
            minimum=j
          
    if(minimum!=i):
        l[i],l[minimum]=l[minimum],l[i]

print(l)