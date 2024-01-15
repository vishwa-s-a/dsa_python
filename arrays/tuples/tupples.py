tup=("geeks")
#this is not a tuple 
print(type(tup))

#this is how to create a tuple with one element
correctTup=('geeks',)
print(type(correctTup))

#using the constructor

tuple_constructor=tuple(('dsa','geeks','for','geeks'))
print(tuple_constructor)


tuple3=('vishwa',)*5
print(tuple3)

#to delete the tuple we use 
del tup


#converting the list to tuple
list1=[90,91,92]
print(tuple(list1))

print(tuple('vishwa'))