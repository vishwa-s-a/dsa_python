class HashTable:
    def __init__(self):
        self.max=10
        self.arr=[None for i in range(self.max)]
    
    def get_hash(self,key):
        h=0
        for i in key:
            h+=ord(i)
        return h%self.max
    
    def __setitem__(self,key,value):
        index=self.get_hash(key)
        if(self.arr[index] is None):
            self.arr[index]=value
        else:
            flag=False
            while not flag:
                index+=1
                index%=self.max
                if(self.arr[index] is None):
                    self.arr[index]=value
                    flag=True

if __name__=='__main__':
    table=HashTable()
    # print(table.get_hash('march 6'))
    # print(table.get_hash('march 17'))
    table['march 6']=12
    table['march 17']=15
    print(table.arr)


