import re
# using \A
x='vsa i am vishwa 9 x z'
y=re.search(r'\Avsa',x)
# print(dir(y))
print(y[0])
print(y)
print(y.start())
print(y.span())
print(y.end())
print(y.string)

print(re.search(r'\bvis',x))#to match the exp in the begining of the word
print(re.search(r'hwa\b',x))#to match the exp in the end of the word
print(re.search(r'\bam',x))# here both the lines gives the same result as am is in beginning and at the end of the word 'am'
print(re.search(r'am\b',x))
print(re.search(r'\Bsh',x))#finds the exp in the middle of the word 
print(re.search(r'\d',x))#here it finds the digits in the expression
print(re.search(r'\D',x))#here it returns if it is not a digit
print(re.search(r'\s',x))#here it searches for white spaces
print(re.search(r'\S',x))
print(re.search(r'\w',x))#here it matches the word characters like a-z and A-Z 0-9 _ underscore characters

print("now seeing the examples of using [] brackets to specify the characters to match".center(103,'*'))
print(re.search(r'[a-v]',x))
print(re.search(r'[0-9]',x))
print(re.findall(r'[x-z]',x))
print(re.findall(r'[^9]',x))

print('using the split method'.center(105,'*'))
print(re.split(r'\s',x))
# now using the maxsplit options
print(re.split(r'\s',x,2))
print(re.split(r'\s',x,1))


print('using the sub method'.center(105,'*'))
print(re.sub('\s','_',x))#substituting the white space with underscore
print(re.sub('\s','_',x,2))#applying the same for only two occurrance of the white space

