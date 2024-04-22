'''
in python to get the min and max value like (-infinity and +infinity)
we use sys.maxsize
max=sys.maxsize
min=-sys.minsize-1
'''
import sys
class TreeNode:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None

def print_inorder(node):
    if(node is None):
        return
    print_inorder(node.left)
    print(node.key,end=' ')
    print_inorder(node.right)

if __name__=='__main__':
    root=TreeNode(3)
    root.left=TreeNode(1)
    root.right=TreeNode(4)
    root.right.left=TreeNode(2)
    print('The given bst: ')
    print_inorder(root)

    first,middle,last=None,None,None
    prev=TreeNode(-sys.maxsize-1)

    def inorder(node):
        global first,middle,last,prev
        if(node is None):
            return 
        inorder(node.left)

        if((prev!=None) and (node.key<prev.key)):
            if(first==None):
                first=prev
                middle=node
            else:
                last=node
        prev=node

        inorder(node.right)

    def recover_bst(node):
        inorder(node)
        if(first!=None and last!=None):
            temp=first.key
            first.key=last.key
            last.key=temp
            #print(first.key,last.key)
        else:
            #print(first.key,middle.key)
            temp=first.key
            first.key=middle.key
            middle.key=temp
    
    recover_bst(root)
    print('\nThe correct bst: ')
    print_inorder(root)
    print('\r')


