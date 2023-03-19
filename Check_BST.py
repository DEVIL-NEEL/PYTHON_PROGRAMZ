def checkBST(node,mini,maxi):
    if node in None:
        return True
    elif node.data<mini or node.data>maxi:
        return False
    else:
        return checkBST(node.left,mini,node.data-1) and checkBST(node.right,node.data+1,maxi)
    
class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None 

