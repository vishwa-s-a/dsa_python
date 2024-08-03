#program for recovery of bst using morris traversal method
from collections import deque
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Tree:
    def __init__(self):
        self.root=None
    
    def display(self,node):
        #inorder display of the tree
        if(node is not None):
            self.display(node.left)
            print(node.data,end=" ")
            self.display(node.right)
    
    def vertical_view(self)->dict:
        q1=deque()
        q2=deque()
        q1.append(self.root)
        q2.append(0)
        d=dict()
        while(len(q1)!=0):
            tempNode=q1.popleft()
            tempLevel=q2.popleft()
            if(tempLevel not in d.keys()):
                d[tempLevel]=list(tempNode.data)
            else:
                d[tempLevel].append(tempNode.data)
            if(tempNode.left is not None):
                q1.append(tempNode.left)
                q2.append(tempLevel-1)
            if(tempNode.right is not None):
                q1.append(tempNode.right)
                q2.append(tempLevel+1)
        return d

    def left_view(self):
        q2=deque()
        q2.append(self.root)
        while(len(q2)!=0):
            level=len(q2)
            for i in range(level):
                temp=q2.popleft()
                if(i==0):
                    print(temp.data,end=" ")
                if(temp.left is not None):
                    q2.append(temp.left)
                if(temp.right is not None):
                    q2.append(temp.right)
    
    def right_view(self):
        q2=deque()
        q2.append(self.root)
        while(len(q2)!=0):
            level=len(q2)
            for i in range(level):
                temp=q2.popleft()
                if(i==(level-1)):
                    print(temp.data,end=" ")
                if(temp.left is not None):
                    q2.append(temp.left)
                if(temp.right is not None):
                    q2.append(temp.right)
    def horizontal_view(self):
        #horizontal view of the tree
        q2=deque()
        q2.append(self.root)
        while(len(q2)!=0):
            for i in range(len(q2)):
                temp=q2.popleft()
                print(temp.data,end=" ")
                if(temp.left is not None):
                    q2.append(temp.left)
                if(temp.right is not None):
                    q2.append(temp.right)
    
    def is_leaf(self,node):
        if(node.left==None and node.right==None):
            return True
        else:
            return False
    def left_traversal(self,node):
        if(node is not None):
            if(not self.is_leaf(node)):
                print(node.data,end=" ")
                self.left_traversal(node.left)
                if(node.left is None):
                    self.left_traversal(node.right)
    
    def right_traversal(self,node):
        if(node is not None):
            if(not self.is_leaf(node)):
                if(node.right is None):
                    self.right_traversal(node.left)
                self.right_traversal(node.right)
                print(node.data,end=" ")
    
    def leaf_traversal(self,node):
        if(node is not None):
            self.leaf_traversal(node.left)
            if(self.is_leaf(node)):
                print(node.data,end=" ")
            self.leaf_traversal(node.right)

    def boundary_traversal(self):
        print(self.root.data,end=" ")
        self.left_traversal(self.root.left)
        self.leaf_traversal(self.root.left)
        self.leaf_traversal(self.root.right)
        self.right_traversal(self.root.right)
if __name__=='__main__':
    l1=input("Enter the tree in array form:\n")
    l2=l1.split(" ")
    tree=Tree()
    tree.root=Node(l2[0])
    q1=deque()
    q1.append(tree.root)
    i=1
    while(i<len(l2)):
        temp1=q1.popleft()
        if(l2[i]!="null"):
            temp1.left=Node(l2[i])
            q1.append(temp1.left)
            i+=1
        else:
            i+=1
        if(l2[i]!="null"):
            temp1.right=Node(l2[i])
            q1.append(temp1.right)
            i+=1
        else:
            i+=1
    print('Inorder traversal of the tree is: ')
    tree.display(tree.root)
    print("\nThe horizontal view of the tree is: ")
    tree.horizontal_view()
    print("\nThe vertical view of the tree is: ")
    vertical=tree.vertical_view()
    vertical_keys=list(vertical.keys())
    for i in sorted(vertical_keys):
        for j in vertical[i]:
            print(j,end=" ")
    print("\nLeft view of the tree is: ")
    tree.left_view()
    print("\nRight view of the tree is: ")
    tree.right_view()
    print("\nBoundary traversal of the tree is: ")
    tree.boundary_traversal()

