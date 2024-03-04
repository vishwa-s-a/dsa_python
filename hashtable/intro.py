'''
here dictionary is used for implementing the hash table and search operations in such data structures 
is usually O(1)

lookup by key is O(1) on average
insertion and deletion is O(1) on average

'''

# here we will see the basic implementation of the hash table(explicitly)
class HashTable:
    def __init__(self):
        self.max=100
        self.arr=[None for i in range(self.max)]

    #this is the important part of the hash table which is hash function
    def get_hash(self,key):
        h=0
        for i in key:
            h+=h+ord(i)
        return h%self.max
    
    def add(self,key,value):
        index=self.get_hash(key)
        self.arr[index]=value

    #__setitem__ is the actual name of the function implemented in dictionary
    def __setitem__(self,key,value):
        index=self.get_hash(key)
        self.arr[index]=value

    def get_value(self,key):
        index=self.get_hash(key)
        return self.arr[index]
    
    #__getitem__ is the actual name of the function implemented in dictionary
    def __getitem__(self,key):
        index=self.get_hash(key)
        return self.arr[index]
    
    def __delitem__(self,key):
        index=self.get_hash(key)
        self.arr[index]=None

if __name__=='__main__':
    table=HashTable()
    table.add('vishwa',23)
    table.add('sachin',25)
    table['aishwarya']=18 # this method calls the __setitem__ function
    print(table.get_value('sachin'))
    del table['vishwa']

    print(table['vishwa']) # this method calls the __getitem__ function