import math
import random

#this variable will contain all prime numbers within 250 in set form 

prime=set()
public_key=None
private_key=None
n=None


#finding all prime numbers within 250
def fill_prime():
    # we use sieve's method of finding prime numbers within a certain range
    global prime
    s=[True]*250
    #as 0 and 1 are not prime we make s[0] s[1] as false
    s[0]=False
    s[1]=False

    for i in range(2,250):
        for j in range(i*2,250,i):
            s[j]=False
    
    for i in range(250):
        if s[i]==True:
            prime.add(i)

def select_random_prime():
    #once we select the random prime number we should remove it from the set
    z=random.randint(0,len(prime)-1)

    #convert prime set to iterable by iter() method
    temp_iter=iter(prime)

    for _ in range(z):
        next(temp_iter)
    
    ret=next(temp_iter)
    #we will remove the element from the set as p!=q
    prime.remove(ret)
    return ret

def set_keys():
    global prime,public_key,private_key,n
    p=select_random_prime()
    q=select_random_prime()
    n=p*q

    #calculating the euler totient phi
    fi=(p-1)*(q-1)

    #finding the value of e(which is nothing but public key) which is less than fi and coprime with fi
    e=2
    while True:
        if math.gcd(e,fi)==1:
            break
        e+=1
    
    public_key=e

    #now finding the private key
    d=2
    while True:
        if (d*e) % fi == 1:
            break
        d+=1
    
    private_key=d

def encrypt(message):# here message will be ascii value of alphabet
    global public_key,n
    e=public_key
    encrypted_val=1
    while e>0:
        encrypted_val*=message
        encrypted_val%=n
        e-=1
    return encrypted_val

def decrypt(encrypted_txt):
    global private_key,n
    d=private_key
    decrypted_val=1
    while d>0:
        decrypted_val*=encrypted_txt
        decrypted_val%=n
        d-=1
    return decrypted_val

if __name__=='__main__':
    # to find and fill all the prime numbers within range of 250
    fill_prime()
    # to set the primary and public keys
    set_keys()

    print('The public key is : ',public_key)
    print('The private key is : ',private_key)
    print('The modulus value is : ',n)
    pt=input("Enter the plain text: ")

    encrypted=[]
    for i in pt:
        encrypted.append(encrypt(ord(i)))
    
    # print(encrypted)
    print('The encrypted text is: ')
    for i in encrypted:
        print(i,end='')
    print('')

    # now decryption part
    s=''
    for i in encrypted:
        s+=chr(decrypt(i))
    print("The decrypted text is : ",s)







