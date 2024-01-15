class Node:
    def __init__(self,data):
        self.prev=None
        self.next=None
        self.data=data
class doubly_linked:
    #this will initialise the head and tail values as None
    def __init__(self):
        self.head=None
        self.tail=None
    def insertAtBeginning(self,data):
        temp_node=Node(data)#creating temp node
        if(self.head is None):
            self.head=temp_node
            self.tail=temp_node
        else:
            temp_node.next=self.head
            self.head.prev=temp_node
            self.head=temp_node
    def insertAtEnd(self,data):
        temp_node=Node(data)
        if(self.tail is None):
            self.head=temp_node
            self.tail=temp_node
        else:
            temp_node.prev=self.tail
            self.tail.next=temp_node
            self.tail=temp_node
    
    def insert_at_position(self,data,position):
        temp_node=Node(data)
        if(position==1):
            doubly_linked.insertAtBeginning(self,data)
        else:
            current_position=1
            current=self.head
            while(current is not None and current_position<position):
                current=current.next
                current_position+=1
            temp_node.next=current
            temp_node.prev=current.prev
            current.prev.next=temp_node
            current.prev=temp_node
    def traverse_list(self):
        temp_node=self.head
        print("Printing the list in normal order: ",end='')
        while(temp_node is not None):
            print(temp_node.data,' ',end='')
            temp_node=temp_node.next
        print('\r')

# now to write the code which will use the above classes
doubly=doubly_linked()
doubly.insertAtBeginning(1)
doubly.insertAtEnd(2)
doubly.insert_at_position(0,1)
doubly.traverse_list()
        