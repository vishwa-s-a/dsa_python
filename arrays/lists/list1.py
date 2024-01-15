l1=['apple','manzanasa']
l2=['father','padre']
t1=('mother','madre')
l3=l1+l2
l1.extend(l2)
l1.extend(t1)
print(l3)
print(l1)
del l2[0]
del l3
print(l2)
# print(l3)
# l1.clear()
print(l1)
for x in l1:
    print(x)
[print(x) for x in l1]

newlist=[x.upper() for x in l1 if x.startswith("p")]
print(newlist)

print([x for x in range(20)])
print([x if x!='padre' else 'abuelo' for x in l1])