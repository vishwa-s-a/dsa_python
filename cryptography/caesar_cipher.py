
def caesar_cipher(txt):
    for i in txt:
        actual_value=ord(i)-97
        cipher_value=((actual_value+3)%26)+97
        print(chr(cipher_value).capitalize(),end='')
    print('\r')
plain_txt=input("Enter the text to be encrypted: ")
print("Cipher text is : ")
caesar_cipher(plain_txt)
