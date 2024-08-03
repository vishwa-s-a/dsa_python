def permutation(arr,k):
    if(k==len(arr)):
        print(arr)
        return
    else:
        for i in range(k,len(arr)):
            arr[k],arr[i]=arr[i],arr[k]
            permutation(arr,k+1)
            arr[i],arr[k]=arr[k],arr[i] # this is for reversing the swap which was done when going down

l=[1,2,3]
print('All possible permutations are: ')
permutation(l,0)
