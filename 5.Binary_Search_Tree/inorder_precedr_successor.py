class Node:
    def __init__(self,key):
        self.right=None
        self.left=None
        self.val=key
def search(root,key):
    if root is None:
        return
    if (root.val==key):
        print(root.val)
    if root.val > key:
        search(root.left,key)
    else:
        search(root.right,key)
    
def insert(root,node):
    if root is None :
        return root
    else:
    
        if root.val > node.val :
            if root .left is None:
                root.left=node
            else:
                insert(root.left,node)
        else:
            if root.right is None:
                root.right=node
            else:
                insert(root.right,node)

   
r = Node(50) 
insert(r,Node(30)) 
insert(r,Node(20)) 
insert(r,Node(40)) 
insert(r,Node(70)) 
insert(r,Node(60)) 
insert(r,Node(80))
search(r,20)