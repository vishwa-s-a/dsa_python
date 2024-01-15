s={1,2,3,13}
s2={'vsa','hello','world'}
print("to proove that sets are unordered and unindexed ")
for x in s2:
    print(x)
# print(s[0])
l1=[1.22,1.33,1.44]

#adding new items
s.add(12)
print(s)
s.update(s2)
print(s)
print(s2)
s.update(l1)
print(s)
s.discard(99)
print("hello programmar")
# s.remove(99)#throws error

for x in s:
    print(x)

#adding two sets or joining two sets
s3=s.union(s2)
print(s3)

#only to keep the common elements from both the sets
#s3.intersection_update(s2)
s4=s3.intersection(s2)
print(s4)

#keep all, but not the duplicates
x={'apple','banana','cherry'}
y={'google','microsoft','apple'}

z=x.symmetric_difference(y)
print(z)

v=z.copy()
r=z#this is referencing
r.pop()
print(r)
print(z)
print(v)


