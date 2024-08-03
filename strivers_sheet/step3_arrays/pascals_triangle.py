#here we are given the row and column number we have to find the value of that 
# row and column in the pascals triangle
# we will use nCr formula

def variation1(row,col):
    n=row-1
    r=col-1
    loop=r
    temp1=1
    temp2=1
    for i in range(loop):
        temp1=temp1*n
        temp2=temp2*r
        n-=1
        r-=1
    return temp1//temp2

def variation2(row):
    n=row
    for i in range(1,n+1,1):
        print(variation1(n,i))
r=5
c=3
print(variation1(r,c))
variation2(r)