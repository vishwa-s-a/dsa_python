
a=input("Enter the first sequence:\n")
b=input("Enter the second sequence:\n")
matrix=[[None for i in range(len(a)+1)] for j in range(len(b)+1)]
for i in range(len(a)+1):
    matrix[0][i]=0
for i in range(len(b)+1):
    matrix[i][0]=0
x=1
y=1

for i in range(len(b)):
    for j in range(len(a)):
        # print("x,y",x,y)
        if(b[i]==a[j]):
            matrix[x][y]=matrix[x-1][y-1]+1
        else:
            matrix[x][y]=max(matrix[x-1][y],matrix[x][y-1])
        y+=1
    x+=1
    y=1
print(matrix)
x=len(b)
y=len(a)
print(x,y)
result=list()
while(y>=0):
    if(matrix[x][y]<=0):
        break
    if(matrix[x][y]==matrix[x][y-1]):
        y-=1
    else:
        result.append(a[y-1])
        y-=1
        x-=1
if(len(result)==0):
    print("None")
else:
    print(result)

