'''
Write a program that can answer following,
i. What was the average temperature in first week of Jan
ii. What was the maximum temperature in first 10 days of Jan
Figure out data structure that is best for this problem
'''

#here the best ds is list, as we to sequentally access the data 
arr=[]
with open("hashtable/nyc_weather.csv","r") as f:
    for line in f:
        tokens=line.split(',')
        try:
            temp=int(tokens[1])
            arr.append(temp)
        except:
            print('invalid temperature')
print(arr)

print('average temp in first week of jan',round(sum(arr[0:7])/7,2))
print('max temp is: ',max(arr[0:10]))
