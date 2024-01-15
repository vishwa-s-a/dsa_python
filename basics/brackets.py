print("Enter the brackets to see if they are balanced")
rules={'(':')','[':']','{':'}'}
def bracketCount(s):
    stack=[]
    for i in s:
        if(i=='(' or i=='[' or i=='{'):
            stack.append(i)
        else:
            if(len(stack)==0 or rules[(stack[-1])]!=i):
                return False
            stack.pop()
    if(len(stack)==0):
        return True

test=input()
# print(test)
str=test.split(",")
# print(str)
for s in str:
    if(bracketCount(s)):
        print("YES")
    else:
        print("NO")