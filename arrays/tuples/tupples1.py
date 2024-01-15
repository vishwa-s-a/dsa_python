tup1=tuple(('dsa','geeks','sir','mam'))
print(tup1)

#updating the tuples
l1=list(tup1)
l1[0]='algos'
tup1=tuple(l1)
print("modified tuple is {}".format(tup1))

#unpacking the tuples
fruits=('apple','bananas','kiwi')
(red,yellow,green)=fruits
print(yellow)

(study,*vsa)=tup1
print(vsa)

print('multiply the tuples')
tup2=fruits*2
print(tup2)