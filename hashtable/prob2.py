'''
Write a program that can answer following,
i. What was the temperature on Jan 9?
ii. What was the temperature on Jan 4?
Figure out data structure that is best for this problem
'''

#here dictionary is the best ds(indirectly we are tring to use hashtable)
dict={}
with open('hashtable/nyc_weather.csv','r') as f:
    for line in f:
        tokens=line.split(',')
        try:
            dict[tokens[0]]=int(tokens[1])
        except:
            print('invalid format')
print(dict)
print('temp on jan 9: ',dict['Jan 9'])
print('temp on jan 4: ',dict['Jan 4'])