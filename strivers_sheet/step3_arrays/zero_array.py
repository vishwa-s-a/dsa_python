def function2(arr):
    col=len(arr[0])
    row=len(arr)
    ind=[]
    for i in arr:
        for j in range(len(i)):
            if(i[j]==0):
                ind.append(j)
    s=set(ind)
    print(ind)
    for i in range(row):
        for j in range(col):
                if(i in s or j in s):
                     arr[i][j]=0
        
    print(arr)


arr=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
function2(arr)