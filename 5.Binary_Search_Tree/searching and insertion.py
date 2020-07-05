class Node:
    def __init__(self,data):
        self.right=None
        self.left=None
        self.data=data

def search(root,key):
    if root is None and root.data==key :
        return root
    
    if root.data > key :
        search(root.left,key)
    search (root.right,key)

root=Node(10)
