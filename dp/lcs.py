s1=input('Enter the first sequence: ')
s2=input('Enter the second sequence: ')
m=len(s1)
n=len(s2)
mat=[[None]*(n+1) for _ in range(m+1)]
for i in range(m+1):
    for j in range(n+1):
        if(i==0 or j==0):
            mat[i][j]=0
for i in range(1,m+1,1):
    for j in range(1,n+1,1):
        if(s1[i-1]==s2[j-1]):
            mat[i][j]=mat[i-1][j-1]+1
        else:
            mat[i][j]=max(mat[i][j-1],mat[i-1][j])
for i in mat:
    print(i)
print('LCS is : ',mat[m][n])