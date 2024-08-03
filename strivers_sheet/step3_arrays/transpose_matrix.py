
def transpose(arr):
    row=len(arr)
    col=len(arr[0])
    i=0
    j=0
    while(i<row):
        j=i
        while(j<col):
            arr[i][j],arr[j][i]=arr[j][i],arr[i][j]
            j+=1
        i+=1
    

arr=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
transpose(arr)
print(arr)