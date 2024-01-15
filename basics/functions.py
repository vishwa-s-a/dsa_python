def naming(*kids):
    print(type(kids))
    for i in kids:
        print(i)

# functions with key value as arguments
def names(child3,child1,child2):
    print('required child is:',child3)
naming('allo','bajji','girani')

names(child1='asdf',child3='harry', child2='ram')
print("kwargs are short of keyword arguments".center(105,'='))
print("we can also send arbitrary kwargs")
def demo_func(**kids):
    print(type(kids))

    print('Last name of the child is',kids['last'])

demo_func(fname='vishwa',last='appaji')

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

# factorial function using the recursion concept
def fact(n):
   if(n>0):
      return n*fact(n-1)
   else:
      return 1

ans=fact(4)
print(ans)