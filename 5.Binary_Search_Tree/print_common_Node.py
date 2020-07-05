class node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
def copy(root1,root2):
    if root1 is None or root2 is None:
        return
    if root1.data==root2.data:
        print(root1.data)
        
    else:
        copy(root1,root2.left) 
        copy(root1,root2.right)
    return(copy(root1.left,root2) or copy(root1.right,root2))

root1=node(8)
root1.left=node(3)
root1.right=node(4)
root2=node(4)
root2.left=node(1)
root2.right=node(3)
copy(root1,root2)

        
