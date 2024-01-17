#finding the leader in the array
def leader(arr,n):
    leader=arr[n-1]# as the right most element is always a leader
    print(leader,end=' ')
    for i in range(n-2,0,-1):
        if(arr[i]>leader):
            leader=arr[i]
            print(leader,end=' ')
    print('\r')
def main():
    arr=[16, 17, 4, 3, 5, 2]
    n=len(arr)
    leader(arr,n)
main()