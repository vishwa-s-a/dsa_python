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

def decrypt():
    pass


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
print("Encrypted text is: ")
encrypt(matrix,k,polygrams)

    