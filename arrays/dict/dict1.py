d1={
"brand":"Ford",
'model':'mustang',
'year':1964
}
print(d1)

#to use the dict constructor
d2=dict(name="John",age=36,country="Norway")
print(d2)

x=d1.keys()
print(x)
y=d1.values()
print(y)
print(d1.get('model'))
print(d1['model'])

z=d1.items()
print(z)

if "model" in d1:
    print("Yes model is there")
if 'ford' in d1:
    print("Yes ford is there")
else:
    print('no ford is there')

d1.update({'year':2021})
print(d1)
d1['year']=2023
print(d1)
d1['color']='mad red'
print(d1)

d1.pop('color')


d1.popitem()
print(d1)

for x in d1:
    print(x)
for x in d1:
    print(d1[x])

for x,y in d1.items():
    print(x,y)

#creating dictionaries inside dictionaries
print("Nested dictionaries".center(105,'='))
children={
    "child1":{
        'name':'sachin',
        'age':26,
    },
    'child2':{
        'name':'aishwarya',
        'age':23,
    },
    'child3':{
        'name':'soumya',
        'age':22,
    }
}
print(children['child1']['name'])
