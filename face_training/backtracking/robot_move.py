def total_moves(cr,cl,r,c):
    if(cr==r and  cl==c):
        return 1
    if(cr>r or cl>c):
        return 0
    return total_moves(cr+1,cl,r,c)+total_moves(cr,cl+1,r,c)

n=int(input())
m=int(input())
print(total_moves(0,0,n-1,m-1))