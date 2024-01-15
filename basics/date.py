import datetime

today=datetime.datetime.now()
rand=datetime.datetime(2002,8,6)

print(today)
print(type(today))
print(today.year)
print(today.month)
print(today.day)
print(today.strftime("%b"))
print(today.strftime("%C"))
print(rand.strftime('%a'))