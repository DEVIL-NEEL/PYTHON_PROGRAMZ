#checking if the tree is symmetric or not
def isMirror(t1, t2):
    if not t1 and not t2: #checking if both nodes are None or not
        return True
    if not t1 or not t2: #checking if any one of the node is None or not
        return False
    return t1.val == t2.val and isMirror(t1.right, t2.left) and isMirror(t1.left, t2.right)

class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
root=node(5)
node.left=node(4)
node.right=node(4)
node.left.left=node(7)
node.right.right=node(7)
print(isMirror(root,root))