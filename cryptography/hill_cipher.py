
def get_cofactor(mat,p,q,temp,n):
    #here mat is original matrix,temp will get the cofactor matrix,n is the size of the received matrix
    #here temp will store the co-factor matrix which will be of size k-1
    i=0
    j=0
    for row in range(n):
        for col in range(n):
            if(row!=p and col!=q):
                temp[i][j]=mat[row][col]
                j+=1
                if(j==n-1):
                    j=0
                    i+=1
    # here the temp will contain the cofactor matrix and we are not returning anything as we are directly modifing the temp variable

def determinant(mat,n):#n will be the size of the matrix for which det to be calculated (varies, as it is a recurssive function)
    #initialize the final answer value
    D=0
    if(n==1):
        return mat[0][0]
    temp=[]#to store the co-factor matrix
    for i in range(k):
        temp.append([None for v in range(k)])#initializing a matrix with None values to store the co-factor matrix
    
    sign=1
    for f in range(n):
        get_cofactor(mat,0,f,temp,n)
        D+=sign*mat[0][f]*determinant(temp,n-1)

        sign=-sign
    return D
    
    
def adjoint_mat(mat,adj):
    if(k==1):
        adj[0][0]=1
        return 
    
    sign=1
    temp=[]# to store the cofactors
    for i in range(k):
        temp.append([None for _ in range(k)])# here we use _ as the iterating variable generally i,j is not used inside the loop so we use _
    
    for i in range(k):
        for j in range(k):
            get_cofactor(mat,i,j,temp,k)

            # sign of adj[j][i] positive if sum of row
            # and column indexes is even.
            if((i+j)%2==0):
                sign=1
            else:
                sign=-1
            
            adj[j][i]=(sign)*(determinant(temp,k-1))
#function to find the inverse of the matrix
def find_multplicative_inverse(num):
    for i in range(500):
        if((i*num)%26==1):
            return i
def find_inverse(matrix,k):
    ## first we will find the determinant of the matrix
    det=determinant(matrix,k)
    det=det%26

    adj=[]
    for i in range(k):
        adj.append([None for _ in range(k)])#here i or j can be used in place of _
    adjoint_mat(matrix,adj)

    #we will copy adj to adjoint for further mod operations
    adjoint=list.copy(adj)
    for i in range(k):
        for j in range(k):
            adjoint[i][j]=adjoint[i][j]%26
    new_det=find_multplicative_inverse(det)

    for i in range(k):
        for j in range(k):
            adjoint[i][j]=(new_det*adjoint[i][j])%26
    
    # print(new_det)
    # print(adjoint)

    return adjoint

def encrypt(matrix,k,polygrams):
    answer=list()
    list2=list()
    for row in polygrams:
        x=0
        temp_sum=0
        j=0
        while(j!=k and x!=k):
           temp_sum+=(ord(row[j])-97)*matrix[j][x]
           j+=1
           if(j==k):
            j=0
            x+=1
            temp_sum=temp_sum%26
            list2.append(chr(temp_sum+97))
            temp_sum=0
        answer.append(list.copy(list2))
        list2.clear()
    
    for i in answer:
        for j in i:
            print(j,end='')
    print('\r')


def decrypt(matrix,k,polygrams):
    inverse_mat=find_inverse(matrix,k)
    encrypt(inverse_mat,k,polygrams)


choice=int(input('Enter 0 to encrypt\tEnter 1 to decrypt\n'))
if(choice==0):
    t=input('Enter the text to encrypt: ')
    txt=t.replace(' ','',-1)
else:
    t=input('Enter the text to decrypt: ')
    txt=t.replace(' ','',-1)

k=int(input('Enter the size of the key: '))
matrix=list()
temp=list()
print('Enter the key matrix: ')
for i in range(k):
    for j in range(k):
        t1=int(input())
        temp.append(t1)
    matrix.append(list.copy(temp))
    temp.clear()
mod_value=len(txt)%k
txt+='x'*mod_value
count=0
polygrams=list()
list1=list()
z=0
while(count<len(txt)):
    list1.append(txt[count])
    z+=1
    count+=1
    if(z==k):
        z=0
        polygrams.append(list.copy(list1))
        list1.clear()
if(choice==0):
    print("Encrypted text is: ")
    encrypt(matrix,k,polygrams)
else:
    print("Decrypted text is: ")
    decrypt(matrix,k,polygrams)
    