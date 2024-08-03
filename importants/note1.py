# we can specify a default value for a non-existent key in a dictionary
d={}
d[1]=99

# if we try to get value of d[2] we get key not found error so we can use get method of dictionary class
print('normal dictionary ans: ',d.get(2,-1)) # here -99 will be returned if the key 2 is not found

## other method of doing the above thing is by using the defaultdict method or class
from collections import defaultdict

dd=defaultdict(lambda:-1) # here the defaultdict takes one argument and it has to be a function, which will be executed if the key is not found in dictionary
dd[1]=99
print('defaultdict ans: ',dd[2])



# to reverse a portion of a list
l=[1,2,3,4,5,6]

#to reverse the list from 1 to 4 is
l[1:5]=l[1:5][::-1]
print('Reversing of portion of list from 1 to 4 index',l)


print('**************************')
print('pow(x,y) is evaluated as x^y')
print('pow(x,y,z) is evaluated as (x^y)%z')

print("to calculate the lcm we can use the math library and method math.lcm(a,b)")
print('Else we can also use this method to find the lcm, lcm=(a*b)//math.gcd(a,b)')

print('**********************************')
print('In set we cannot add other set or a list, but we can add a tuple in set')

print('\n in general set operations take log(n) time where n is the number of elements in set')

print('\n if d is a dictionary then d.popitem() removes an arbitrary item or element (usually the last item in dictionary)')

print('\n in dictionary d, d.setdefault(key,None) if in the dictionary key is found then it prints its value, else it will create new item with this key and value as None')