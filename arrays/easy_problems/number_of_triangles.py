# to calculate the number of triangles in a array
# condition is the sum of any two sides always greater than third side

#this is the naive method for this problem with time complexity O(n^3)
def naive_method(arr,n):
    count=0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if(arr[i]+arr[j]>arr[k] and arr[i]+arr[k]>arr[j] and arr[k]+arr[j]>arr[i] ):
                    count+=1
    return count

#now we will have a efficient method using sorted array
def pointer_solution(arr,n):
    count=0
    arr.sort()
    for i in range(n-1,0,-1):
        l=0
        r=i-1
        while(l<r):
            if(arr[l]+arr[r]>arr[i]):
                count+=r-l# we will get the difference between l and r pointer as our count of the triangles
                r-=1
            else:
                l+=1
    return count

def main():
    list1=[10, 21, 22, 100, 101, 200, 300]
    n=len(list1)
    print('naive method answer: ',naive_method(list1,n))
    print('Double pointer answer: ',pointer_solution(list1,n))

main()