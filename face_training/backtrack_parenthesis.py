'''
Backtracking method is used in this problem to generate this parenthesis pattern
pantangel.apul;
'''
def generateParenthesis(list,pos,n,o,c):
    if(o==n and c==n):
        for i in list:
            print(i,end="")
        print(" ")
        return
    if(o<n):
        list[pos]="("
        generateParenthesis(list,pos+1,n,o+1,c)
    if(o>c):
        list[pos]=")"
        generateParenthesis(list,pos+1,n,o,c+1)

n=int(input())
list=[""]*2*n
generateParenthesis(list,0,n,0,0)