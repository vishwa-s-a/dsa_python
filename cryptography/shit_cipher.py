
def caesar_cipher(txt,key):
    for i in txt:
        actual_value=ord(i)-97
        cipher_value=((actual_value+key)%26)+97
        print(chr(cipher_value).capitalize(),end='')
    print('\r')
plain_txt=input("Enter the text to be encrypted: ")
key=int(input("Enter the key for encryption: "))
if(key<0 or key>25):
    exit(0)
print("Cipher text is : ")
caesar_cipher(plain_txt,key)
