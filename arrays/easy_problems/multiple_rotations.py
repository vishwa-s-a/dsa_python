def multiple_rotations(arr,n):
    n=n%len(arr)
    p=len(arr)
    for i in range(0,len(arr)):
        print(arr[(n+i)%p],end=' ')
    print('\r')


str_arr=input('Enter the list: ')
temp_arr=str_arr.split(',')
arr=list()
for i in range(0,len(temp_arr)):
    arr.append(int(temp_arr[i]))

while(True):
    #run infinite loop for user
    n=int(input('Enter the number of rotation: '))
    if(n==99):
        break
    multiple_rotations(arr,n)