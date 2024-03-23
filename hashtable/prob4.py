class HashTable:
    def __init__(self):
        self.max=10
        self.arr=[None for i in range(self.max)]
    
    def get_hash(self,key):
        h=0
        for i in key:
            h+=ord(i)
        return h%self.max
    
    def get_empty_space(self):
        count=0
        for i in self.arr:
            if i is None:
                count+=1
        return count
    
    def __setitem__(self,key,value):
        index=self.get_hash(key)
        if(self.arr[index] is None):
            self.arr[index]=(key,value)
        elif self.arr[index][0]==key:
            self.arr[index]=(key,value)
        else:
            if(self.get_empty_space()==0):
                raise Exception('Hash table is full')
                return
            flag=False
            while not flag:
                index+=1
                index%=self.max
                if(self.arr[index] is None):
                    self.arr[index]=(key,value)
                    flag=True
    
    def __getitem__(self,key):
        index=self.get_hash(key)
        if self.arr[index] is not None:
            element=self.arr[index]
            if(element[0]==key):
                return element[1]
            else:
                temp=index+1
                while(temp!=index):
                    element=self.arr[temp]
                    if(element[0]==key):
                        return element[1]
                    else:
                        temp=(temp+1)%self.max
                else:
                    print("item doesnt exist")


if __name__=='__main__':
    table=HashTable()
    # print(table.get_hash('march 2'))
    # print(table.get_hash('march 13'))
    table['march 1']=11
    table['march 4']=14
    table['march 2']=12
    table['march 3']=13
    table['march 5']=15
    table['march 17']=15
    table['march 6']=18
    table['march 12']=33
    table['march 13']=44
    table['march 14']=55

    # this following line will give a exception of hash table full
    # uncomment it to see
    # table['march 15']=66
    print(table.arr)
    # print(table.get_empty_space())
    print(table['march 28'])


