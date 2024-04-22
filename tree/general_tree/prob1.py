class TreeNode:
    def __init__(self,name,pos):
        self.name=name
        self.pos=pos
        self.children=[]
        self.parent=None

    def add_children(self,node):
        node.parent=self
        self.children.append(node)
    
    def get_level(self,node):
        if(node.parent== None):
            return 0
        return 1+self.get_level(node.parent)
    
    def print_tree_1(self,node):
        level=self.get_level(node)
        #print(level)
        prefix='   '*level+'|--' if node.parent else ""
        print(prefix,node.name)
        if(len(node.children)==0):
            return
        for i in node.children:
            self.print_tree_1(i)
    
    def print_tree_2(self,node):
        level=self.get_level(node)
        #print(level)
        prefix='   '*level+'|--' if node.parent else ""
        print(prefix,node.pos)
        if(len(node.children)==0):
            return
        for i in node.children:
            self.print_tree_2(i)
    
    def print_tree_3(self,node):
        level=self.get_level(node)
        #print(level)
        prefix='   '*level+'|--' if node.parent else ""
        print(prefix,node.name+' '+'('+node.pos+')')
        if(len(node.children)==0):
            return
        for i in node.children:
            self.print_tree_3(i)
    
    def print_tree_4(self,node,l):
        level=self.get_level(node)
        if(level>l):
            return
        #print(level)
        prefix='   '*level+'|--' if node.parent else ""
        print(prefix,node.name+' '+'('+node.pos+')')
        if(len(node.children)==0):
            return
        for i in node.children:
            self.print_tree_4(i,l)

if __name__=='__main__':
    root=TreeNode('Nilupul','CEO')
    temp1=TreeNode('Chinmay','CTO')
    temp3=TreeNode('vishwa','Infra Head')
    temp3.add_children(TreeNode('Dhawal','Cloud Manager'))
    temp3.add_children(TreeNode('Abhijit','App manager'))
    temp1.add_children(temp3)
    temp1.add_children(TreeNode('Aamir','Application Head'))
    temp2=TreeNode('Gels','HR head')
    temp2.add_children(TreeNode('peter','Recruitment manager'))
    temp2.add_children(TreeNode('waqas','policy manager'))
    #tree.print_tree_1(tree.root)
    root.add_children(temp1)
    root.add_children(temp2)
    root.print_tree_1(root)
    print('\n')
    root.print_tree_2(root)
    print('\n')
    root.print_tree_3(root)
    print('\n')
    root.print_tree_4(root,1)
