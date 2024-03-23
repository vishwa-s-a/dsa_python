num1=input().split(' ')
num2=input().split(" ")
num1.sort()
g=0

def gcd(num1,num2):
    if(num2==0):
        return abs(num1)
    else:
        return gcd(num2,num1%num2)
  
g=gcd(int(num2[0]),int(num2[1]))
for i in range(2,len(num2)):
    g=gcd(g,int(num2[i]))


count=0
it=iter(set(num1))
for i in range(len(set(num1))):
    value=int(next(it))
    if(g%value!=0):
        count+=1
if(count==len(set(num1))):
    print('-1')
else:
    print(count)