def encryption(pt,key,n):
    s=[i for i in range(0,2**n)]
    p=[pt[i:i+n] for i in range(0,len(pt),n)] # breaking the input into the length of n as required
    k=[key[i:i+n] for i in range(0, len(key),n)]


    # now converting the p and k to decimals
    for i in range(0,len(p)):
        p[i]=int(p[i],2)
        k[i]=int(k[i],2)
    print("plain text in decimal format(in length of n): ",p)
    print("key in decimal format(in length of n): ",k)

    #now creating a temporary vector required for key scheduling algorithm(ksa)
    t=[k[i%len(k)] for i in range(len(s))]
    # print(t)

    def ksa():
        #this function is used to generate the keys 
        j=0
        N=len(s)
        for i in range(N):
            j=(j+s[i]+t[i])%N

            s[i],s[j]=s[j],s[i]

        print("The initial permutation array is : ",s)
    ksa()

    #now key stream generation
    def key_stream_gen():
        N = len(s)
        i = j = 0
        global key_stream
        key_stream = []

        for z in range(len(k)):
            i=(i+1)%N
            j=(j+s[i])%N

            s[i],s[j]=s[j],s[i]
            temp=(s[i]+s[j])%N
            key_stream.append(s[temp])
        print("Key stream : ", key_stream)

    key_stream_gen()

    # Performing XOR between generated key stream and plain text
    def cipher():
        global cipher_text
        cipher_text=""
        for i in range(len(k)):
            temp=p[i]^key_stream[i]
            cipher_text += '0'*(n-len(bin(temp)[2:]))+bin(temp)[2:]
    
    cipher()
    return cipher_text

#now the decryption part
def decryption(ct,key,n):
    print("***************** Decryption part ******************".center(105))
    return encryption(ct,key,n)

if __name__=='__main__':
    #declaring these as global variables
    # pt=input()
    # key=input()
    # n=int(input())
    pt="1111000000001111"
    key="0101010111001010"
    n=4
    print("***************** Encryption part ******************".center(105))
    ct=encryption(pt,key,n)
    print("")
    print('Cipher text is: ',cipher_text)
    p=decryption(ct,key,n)
    print("")
    print('Plain text is : ',p)