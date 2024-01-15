import random
x=1
y=2.89
z=5j
print(type(x),type(y),type(z))

a=int(y)#cast float to int
b=float(x)# cast int to float
c=complex(x)
d=complex(y)

print(a,b,c,d)
r=random.randrange(0,10)
r=random.randint(0,3)
print(r)

multi="""This is a multi line 
can be extended for as many lines as possible
good exmaple"""

for x in "bananas":
    print(x)