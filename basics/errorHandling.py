x=5
try:
    print(x)
except :
    print("X is not defined")
else:
    print('x is defined')
finally:
    print('i am exiting the program')

print('Raising the errors'.center(105,'*'))

# below line of code is used to raise a exception
# if not type(x) is str:
#     raise Exception('X is not a string')

# this line is used to raise a particular type of error
if type(x) is not str:
    raise TypeError('x is not a string')