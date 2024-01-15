num1=[12,1,98,23,26,3]
print(sorted(num1))
print(num1)
num2=[1,2,3,4,5,6]

#function to check if function is sorted or not
def isSorted(list1):
    if(list1==sorted(list1)):
        return True
    else:
        return False

result=isSorted(num2)
print(result)

#to get the index of the list where the list is changing
def getIndex(list1,opt):
    if(opt=='a'):
        for i in range(0,len(list1)-1):
            if(list1[i+1]<list1[i]):
                return len(list1)-(i+1)
        return 0
    else:
        for i in range(0,len(list1)-1):
            if(list1[i+1]>list1[i]):
                return len(list1)-(i+1)
        return 0

#to check if the list is circularly rotated and sorted
def circularSort(list1):
    if(isSorted(list1)):
        print("list is sorted in ascending order and rotated for",len(list1),"times")
        return
    if(list1[0]<list1[1]):
        print("list is in ascending order")
        print("Rotated for",getIndex(list1,'a'),"times")
    elif(list1[0]>list1[1]):
        print("list is in descending order")
        print("Rotated for",getIndex(list1,'d'),"times")

test=[3,2,1,6,5,4]
circularSort(test)
