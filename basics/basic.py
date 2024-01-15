print("Hello world")
print("good ")
print("bye ")

print("Vishwa Shivanand ",end="")#we add this end="" to avoid new line character after this print statement
print("Appaji ")

l1=['11','12','13']
x,y,z=l1

print(x,y,z)
print(x+y+z)

#this is a global variable
x="good morning"
def myFunc():
    global x
    x="fantastic"
    print("Python is :",x)
myFunc()
print(x)

z=range(6)
print(z)
w=frozenset({'apple','banana'})

print(w)


vishwa=dict(name="vishwa",age=21)
print(vishwa)

b=bool(5)
print(b)

x=bytes(5)
print(x)



y=memoryview(x)
print(y)