i=0
while i<6:
    i+=1
    if i==3:
        continue
    print(i)

j=0
while j<6:
    print(j)
    j+=1
else:
    print(j,"j is greater than 6")


for i in range(2,10):
    print('for loop',i)
else:
    print('loop finished running')

# if a break statement is in for loop then we dont see the else block executing after the for loop 
for i in range(3,20,3):
    print('for loop with break',i)
    if(i==15):
        break
else:
    print('i will not be executed')


#avoiding errors by putting a pass statements
print('using pass statements '.center(105,'='))
for i in range(6):
    pass