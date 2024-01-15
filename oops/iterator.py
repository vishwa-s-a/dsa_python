from functions import fact
import platform

name='vishwa'
it=iter(name)
print(next(it))
print(next(it))

# ans=fact(4)
# print(ans)
print(platform.system())
print(dir(platform))
print(dir(fact))
