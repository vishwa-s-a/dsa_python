class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None
    
    def add_children(self,child):
        #here child is also of TreeNode class object
        child.parent=self
        self.children.append(child)
    
    def get_level(self,node):
        if(node.parent==None):
            return 0
        return 1+self.get_level(node.parent)
    
    def print_tree(self,node):
        level=self.get_level(node)
        prefix='  '*level+'|--' if node.parent else ""
        print(prefix,node.data)
        if(len(node.children)==0):
            return
        for i in node.children:
            self.print_tree(i)

def build_product_tree():
    root=TreeNode('electronics')

    laptop=TreeNode('laptop')
    laptop.add_children(TreeNode('Mac'))
    laptop.add_children(TreeNode('Inspiron'))

    phone=TreeNode('phone')
    phone.add_children(TreeNode('iphone'))
    phone.add_children(TreeNode('galaxy'))

    root.add_children(laptop)
    root.add_children(phone)

    #print(root.get_level(root))
    return root
if __name__=='__main__':
    root=build_product_tree()
    root.print_tree(root)