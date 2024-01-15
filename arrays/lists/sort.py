l1=["orange", "mango", "kiwi", "pineapple", "banana"]
l1.sort(reverse=True)

l2=[100, 50, 65, 82, 23]
# l2.sort(reverse=True)
print(l1)
print(l2)

def myfunc(n):
    return abs(50-n)
l2.sort(key=myfunc)# we are defining a function to sort the list according to how much the number is nearest to the given element of the list
print(l2)

print("case sensitivity".center(100,"="))
l3=["banana", "Orange", "Kiwi", "cherry"]
l3.sort()
print(l3)

l3.sort(key=str.lower)
print(l3)
l3.reverse()
print(l3)