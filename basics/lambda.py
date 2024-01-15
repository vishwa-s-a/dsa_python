x=lambda a:a+10
print(x(5))

y=lambda a,b:a*b
print(y(10,20))

print("main use of the lambda expression is to create a anonymous functions for a short period of time")
print('anonymous lambda functions'.center(105,'='))
def firstFunction(n):
    return lambda a: a*n
secondF=firstFunction(10)
print(secondF(2))