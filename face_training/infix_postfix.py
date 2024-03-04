exp=input()
l1=list(exp)
l2=[]
priority={
    '(':0,
    '+':1,
    '-':1,
    '*':2,
    '/':2,
    '^':3
}
for i in l1:
    if i.isalnum():
        print(i,end="")
    elif i=='(':
        l2.append(i)
    elif i==')':
        for i in l2:
            if i=='(':
                l2.pop()
                break
            print(l2.pop(),end="")
    else:
        if len(l2)==0:
            l2.append(i)
        elif len(l2)!=0 and priority[i]>priority[l2[-1]]:
            l2.append(i)
        elif len(l2)!=0 and priority[i]==priority[l2[-1]]:
            if i=='^':
                l2.append(i)
            else:
                print(l2.pop())
                l2.append(i)
        else:
            while True and len(l2)!=0:
                if priority[i]<priority[l2[-1]]:
                    print(l2.pop(),end="")
                elif priority[i]==priority[l2[-1]]:
                    if i=='^':
                        l2.append(i)
                    else:
                        print(l2.pop())
                        l2.append(i)
                else:
                    l2.append(i)
                    break