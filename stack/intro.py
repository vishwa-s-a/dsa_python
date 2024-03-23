# using list as stack is not recommended as lists are dynamic array and occupy a lot of space when needed
# so we should use collections.deque

from collections import deque

stack=deque()
l=['[','(','{']
l2=[']','}',')']
s=input()
flag=False
for i in s:
    if(i in l):
        stack.append(i)
    elif (i in l2):
        if(len(stack)!=0):
            stack.pop()
        else:
            flag=True
            break
if(flag):
    print('False')
else:
    if(len(stack)==0):
        print('True')
