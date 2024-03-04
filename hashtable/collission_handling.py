#handling collissions using linked list(separate chaining)

class HashTable:
    def __init__(self):
        self.max=100
        self.arr=[[] for i in range(self.max)]

    #this is the important part of the hash table which is hash function
    def get_hash(self,key):
        h=0
        for i in key:
            h+=ord(i)
        return h%self.max

    def __setitem__(self,key,value):
        index=self.get_hash(key)
        found=False
        for idx,element in enumerate(self.arr[index]):
            #if already exists then modify
            if len(element)==2 and element[0]==key:
                self.arr[index][idx]=(key,value)
                found=True
                break
        if not found:
            self.arr[index].append((key,value))#if not found then add
    
    def __getitem__(self,key):
        index=self.get_hash(key)
        for element in self.arr[index]:
            if(element[0]==key):
                return element[1]
    
    def __delitem__(self,key):
        index=self.get_hash(key)
        
        for idx,element in enumerate(self.arr[index]):
            if(element[0]==key):
                del self.arr[index][idx]

if __name__=='__main__':
    table=HashTable()

    table['march 6']=120
    table['may 2']=458

    print(table['march 6'])
    print(table['may 2'])
    del table['march 6']
    print(table.arr)