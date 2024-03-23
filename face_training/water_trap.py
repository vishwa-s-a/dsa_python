#this program finds the amount of water that can be trapped in gap formed within the 2 elements of the array
# if the array is [7,2,5]
# then between 7 and 2, 5 units of water can be stored
# then between 7 and 5, 2 units of water can be stored

num=input().split(' ')
for i in range(len(num)):
    num[i]=int(num[i])
left_right=[0 for i in range(len(num))]
right_left=[0 for i in range(len(num))]
left_right[0]=num[0]
right_left[-1]=num[-1]
for i in range(1,len(num)):
    if(left_right[i-1]>num[i]):
        left_right[i]=left_right[i-1]
    else:
        left_right[i]=num[i]
#print(left_right)

for i in range(len(num)-2,-1,-1):
    if(right_left[i+1]>num[i]):
        right_left[i]=right_left[i+1]
    else:
        right_left[i]=num[i]
#print(right_left)

result=[]
for i in range(len(num)):
    m=min(left_right[i],right_left[i])
    result.append(m-num[i])
print('result array: ',result)
print('the sum is: ',sum(result))