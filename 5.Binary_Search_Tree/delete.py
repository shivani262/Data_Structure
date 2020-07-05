class Node:
    def __init__(self,key):
        self.right=None
        self.left=None
        self.val=key

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
def inorder(root): 
	if root: 
		inorder(root.left) 
		print(root.val, end="  ") 
		inorder(root.right) 


def delete(root,key):
    if root is None:
        return root
        
    elif root.val > key:
        root.left=delete(root.left,key)
    elif root.val < key:
        root.right=delete(root.right,key)
    else:
        if root.left is None:
            temp=root.right
            root=None
            return temp
        elif root.right is None:
            temp=root.left
            root=None
            return temp
        temp=minele(root.right)
        root.val=temp.val
        root.right=delete(root.right,temp.val)
    return root 

def minele(root):
    current=root
    while(current.left is not None):
        current=current.left
    return current
r = Node(50) 
insert(r,Node(30)) 
insert(r,Node(20)) 
insert(r,Node(40)) 
insert(r,Node(70)) 
insert(r,Node(60)) 
insert(r,Node(80)) 
inorder(r)
delete(r,50)
print()
inorder(r)
