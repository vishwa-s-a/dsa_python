def encrypt(txt_mod,key_mod):
    length=len(txt_mod)
    k=list()
    pt=list()
    ct=list()
    for i in range(length):
        pt.append(ord(txt_mod[i])-97)
        k.append(ord(key_mod[i%len(key_mod)])-97)
        ct.append(chr((k[-1]+pt[-1])%26+97))
    for i in ct:
        print(i.upper(),end='')
    print('\r')

def decrypt(txt_mod,key_mod):
    length=len(txt_mod)
    k=list()
    pt=list()
    ct=list()
    for i in range(length):
        ct.append(ord(txt_mod[i])-97)
        k.append(ord(key_mod[i%len(key_mod)])-97)
        pt.append(chr((ct[-1]-k[-1])%26+97))
    for i in pt:
        print(i.upper(),end='')
    print('\r')

def main():
    choice=int(input("Enter 0 for encryption:\nEnter 1 for decryption:\n"))
    if(choice==0):
        txt=input("Enter the plain text: ")
    else:
        txt=input('Enter the cipher text: ')
    key=input("Enter the key: ")
    txt_mod=txt.replace(' ','',-1)
    key_mod=key.replace(' ','',-1)
    if(choice==0):
        print("Encrypted text is : ")
        encrypt(txt_mod,key_mod)
    else:
        print('Decrypted text is: ')
        decrypt(txt_mod,key_mod)
main()