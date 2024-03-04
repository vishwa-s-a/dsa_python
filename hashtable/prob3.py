'''
 poem.txt Contains famous poem "Road not taken" by poet Robert Frost. 
 You have to read this file in python and print every word and its count as show below. 
 Think about the best data structure that you can use to solve this problem and figure out why you selected that specific data structure.

'''
#use dictionary
words={}
with open('hashtable/poem.txt','r') as file:
    for line in file:
        # print(type(line))
        line=line.replace('\n','')
        tokens=line.split(' ')
        for token in tokens:
            if token in words:
                words[token]+=1
            else:
                words[token]=1

for i in words:
    print(f"{i}: {words[i]}")