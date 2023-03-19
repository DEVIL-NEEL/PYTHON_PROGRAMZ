def height(node):
    if node==None:
        return 0 
    elif node.left==None and node.right==None:
        return 0
    else:
        return max(height(node.left)+1,height(node.right)+1) 
    
class node:
    def __init__(self,data):
        self.data=data
        self.left=None 
        self.right=None
        
root=node(3)
root.left=node(2)
root.right=node(5)
root.left.left=node(1)

print(height(root))