def find_index(element,mat):
    for i,row in enumerate(mat):
        try:
            j = row.index(element)
            return i, j
        except ValueError:
            pass
def encrypt(dig,mat):
    answer=''
    for i in dig:
        t1=i[0]
        t2=i[1]
        if(t1=='i' or t1=='j'):
            t1='ij'
        if(t2=='i' or t2=='j'):
            t2='ij'
        position1=find_index(t1,mat)
        position2=find_index(t2,mat)
        x1=position1[0]
        y1=position1[1]

        x2=position2[0]
        y2=position2[1]

        if(x1==x2):
            y1=(y1+1)%5
            y2=(y2+1)%5
            answer=answer+(mat[x1][y1])+mat[x2][y2]
        elif(y1==y2):
            x1=(x1+1)%5
            x2=(x2+1)%5
            answer=answer+mat[x1][y1]+mat[x2][y2]
        else:
            answer=answer+mat[x1][y2]+mat[x2][y1]
    print(answer.replace('j','',-1))

def decrypt(dig,mat):
    answer=''
    for i in dig:
        t1=i[0]
        t2=i[1]
        if(t1=='i' or t1=='j'):
            t1='ij'
        if(t2=='i' or t2=='j'):
            t2='ij'
        position1=find_index(t1,mat)
        position2=find_index(t2,mat)
        x1=position1[0]
        y1=position1[1]

        x2=position2[0]
        y2=position2[1]

        if(x1==x2):
            y1=(y1-1)%5
            y2=(y2-1)%5
            answer=answer+(mat[x1][y1])+mat[x2][y2]
        elif(y1==y2):
            x1=(x1-1)%5
            x2=(x2-1)%5
            answer=answer+mat[x1][y1]+mat[x2][y2]
        else:
            answer=answer+mat[x1][y2]+mat[x2][y1]
    new_answer=answer.replace('j','',-1)
    if(new_answer[-1]=='x'):
        new_answer=new_answer[0:len(new_answer)-1]
    print(new_answer)
choice=int(input("Enter 0 to encrypt\tEnter 1 to decrypt\n"))
if(choice==1):
    txt=input('Enter the cipher text: ')
    key=input('Enter the key: ')
    plain_txt=list(txt)
else:
    txt=input('Enter the plain text: ')
    key=input('Enter the key: ')
    temp_txt=txt.replace(' ','',-1)
    plain_txt=list(temp_txt)#converting the string to list, as string is not modifiable

digrams=list()

# generating the digrams for the algorithm
for i in range(0,len(plain_txt),2):
    temp=list()
    try:
        r=plain_txt[i]
        s=plain_txt[i+1]
        if(r==s):
            plain_txt.insert(i+1,'x')
            s='x'
        temp.append(r)
        temp.append(s)
        digrams.append(list.copy(temp))
    except(IndexError):
        temp.append(plain_txt[i])
        temp.append('x')
        digrams.append(list.copy(temp))
    finally:
        temp.clear()
# print('Digrams are: ')
# print(digrams)

# now generating the 5x5 matrix using the key
key_mod=key.replace(' ','',-1)#remove all space character
new_key=''
for j in key_mod:
    if j not in new_key:
        new_key+=j
    else:
        pass
matrix=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]#initiailizing a 5x5 matrix
row,col=0,0
temp=list()

#filling the 5x5 matrix with initial key characters
for i in range(0,len(new_key)):
    if(new_key[i]=='i'):
        temp.append('ij')
        col+=1
    elif(new_key[i]=='j'):
        pass
    else:
        temp.append(new_key[i])
        col+=1
    if(col==5):
        matrix[row]=list.copy(temp)#we have to copy the temp list not to directly reference the list as it is varing continously
        temp.clear()
        col=0
        row+=1
        # temp.clear()
    elif(i==(len(new_key)-1)):
        t1=5-col
        temp2=temp+([0]*t1)
        matrix[row]=list.copy(temp2)
#now filling the remaining places in 5x5 matrix
a=97
mat_key=new_key
i=row
j=col
while(i<5):
    alphabet=chr(a)
    # print(alphabet)
    if(alphabet not in mat_key and alphabet!='j'):
        # print(alphabet)
        if(alphabet=='i'):
            alphabet='ij'
        mat_key+=alphabet
        matrix[i][j]=alphabet
        j+=1
    a+=1
    if(j==5):
        j=0
        i+=1
# print("The 5x5 matrix is : ")
# print(matrix)
if(choice==0):
    print('\nThe encrypted text is: ')
    encrypt(digrams,matrix)
else:
    print('\nThe decrypted text is: ')
    decrypt(digrams,matrix)
