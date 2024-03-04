class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None
    
    def insertAtStart(self,data):
        node=Node(data,self.head)
        self.head=node
    
    def insertAtEnd(self,data):
        node=Node(data)
        if(self.head is None):
            self.head=node
            return
        itr=self.head
        while(itr.next is not None):
            itr=itr.next
        itr.next=node

    def insertValues(self, data_values):
        #here data_values can be a list or anything similar
        for i in data_values:
            self.insertAtEnd(i)

    def get_length(self):
        itr=self.head
        if(itr is None):
            print('length of list is 0')
            return
        count=0
        while itr:
            count+=1
            itr=itr.next
        print(f'length of the list is {count}')
    
    def remove_at(self,index):
        itr=self.head
        temp=self.head
        if(index==0):
            self.head=self.head.next
            return
        itr=self.head.next
        count=1
        while itr:
            if(count==index):
                temp.next=itr.next
                itr.next=None
                del itr
                break
            else:
                count+=1
                temp=itr
                itr=itr.next
        if(index>count):
            print('the specified index does not exist')

    def insert_at(self,index,data):
        itr=self.head.next
        temp=self.head
        if(index==0):
            self.insertAtStart(data)
            return
        count=1
        node=Node(data)
        while itr:
            if(count==index):
                node.next=itr
                temp.next=node
                break
            else:
                count+=1
                temp=itr
                itr=itr.next
        if(index>count):
            print('the specified index does not exist')

    def insert_after(self,data_after,data_inserted):
        # in this function we will insert data_inserted after the first occurrence of the data_after
        temp=self.head
        itr=self.head.next
        node=Node(data_inserted)
        flag=False
        while temp:
            if(temp.data==data_after):
                temp.next=node
                node.next=itr
                flag=True
                break
            else:
                temp=itr
                if(itr.next is None):
                    break
                itr=itr.next
        if(not flag):
            print('Given data doesnt exit')

    def remove_first_occurance(self,data):
        count=0
        itr=self.head
        flag=False
        while itr:
            if(itr.data==data):
                self.remove_at(count)
                flag=True
            else:
                count+=1
                itr=itr.next
        if(not flag):
            print('The data doesnt exit')

    def display(self):
        itr=self.head
        if(itr is None):
            print('Linked list is empty')
            return
        while itr:
            print(itr.data,end='-->')
            itr=itr.next

## this is one way of defining what should run when the main() function is executed

# def main():
#     print(__name__)
#     list=LinkedList()
#     list.insertAtStart(4)
#     list.insertAtStart(3)
#     list.insertAtStart(2)
#     list.display()
# main()
            
## now we use the __name__ variable to define what should run when this python script runs
# __name__ will be set as __main__ if this file is run as standalone python script 
# if imported in another file then the __name__ will be set as the file's name to indicate which file's code is running

if __name__=='__main__':
    list=LinkedList()
    list.insertAtStart(4)
    list.insertAtStart(3)
    list.insertAtStart(2)
    list.insertAtEnd(5)
    list.display()
    print('')
    list.get_length()
    list.remove_at(5)
    list.insert_at(2,99)
    list.display()
    print('')


    #one more linked list
    list2=LinkedList()
    list2.insertValues(['vishwa','Shivanand',"appaji"])
    list2.insert_at(1,'Sachin')
    list2.insert_after('vishwa','shivanand appaji')
    list2.remove_first_occurance('vishwa')
    list2.display()
    print('')
