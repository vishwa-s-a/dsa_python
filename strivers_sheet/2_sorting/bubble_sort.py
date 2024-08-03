'''
pushes the max element to the last by adjacent swaps

* worst time complexity is o(n^2) also the average time complexity

* but we can optimize the code, in some case we can see that if the input is already sorted then 
  time complexity is o(n) and to identify this we check the number of swaps in the loop
  if zero swaps then the array is sorted so we exit

* best time complexity is o(n)
'''
l1=input('enter the array: ').split(",")
l=[eval(i) for i in l1]
swaps=0
for i in range(len(l)-1,0,-1):
    for j in range(0,i,+1):
        if(l[j]>l[j+1]):
            l[j],l[j+1]=l[j+1],l[j]
            swaps+=1
    if(swaps==0):
        print('array already sorted ')
        break
print(l)