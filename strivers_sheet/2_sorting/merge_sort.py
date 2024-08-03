'''

this code is written by me and its correct
this is much more well optimized and good performing algo


'''

def merge(arr,start,mid,end):
    for i in range(mid+1,end+1,1):
        pointer=i
        for j in range(i-1,start-1,-1):
            if(arr[pointer]<arr[j]):
                arr[pointer],arr[j]=arr[j],arr[pointer]
                pointer=j
    # print(arr)
def merge_sort(arr,start,end):
    if(start!=end):
        mid=(start+end)//2
        merge_sort(arr,start,mid)
        merge_sort(arr,mid+1,end)
        merge(arr,start,mid,end)
        
# l1=input('Enter the array: ').split(",")
# l=[eval(i) for i in l1]
l=[6334,4098,7968,4523,277,6956,4560,2062,5705,5743,879,5626,9961,491,2995,741,4827]
n=len(l)
merge_sort(l,0,n-1)
print(l)

