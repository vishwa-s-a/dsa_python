class Node:
    def __init__(self,key) -> None:
        self.key=key
        self.left=None
        self.right=None
def insert(node,val):
    if(node is None):
        return Node(val)
    if(node.key>val):
        node.left=insert(node.left,val)
    elif(node.key<val):
        node.right=insert(node.right,val)
    
    return node

def search(node,key):
    if(node is None or node.key==key):
        return node
    
    if(node.key>key):
        return search(node.left,key)
    
    return search(node.right,key)

def inorder(node):
    if(node is None):
        return 
    inorder(node.left)
    print(node.key)
    inorder(node.right)
root=None
root=insert(root,50)
insert(root, 30)
insert(root, 20)
insert(root, 40)
insert(root, 70)
insert(root, 60)
insert(root, 80)
inorder(root)

key = 60
 
# Searching in a BST
if search(root, key) is None:
    print(key, "is not found")
else:
    print(key, "is found")