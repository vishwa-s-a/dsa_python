import json
import re
x='{"name":"vishwa","age":23}'
y=json.loads(x)
print(y,type(y))
print(y['name'])

z={
    'name':'vishwa',
    'emp_id':1234,
    'age':23,
    'place':'ilkal'
}
print(type(z))   
a=json.dumps(z,indent=3,sort_keys=True)
print(a,type(a))
print(dir(json))
# help(json.loads)
# print(json.loads.__doc__)
print(dir(re))
# help(re.match)