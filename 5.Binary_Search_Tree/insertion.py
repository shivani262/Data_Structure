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
                #print(root.left.val)
            else:
                insert(root.left,node)
        else:
            if root.right is None:
                root.right=node
               # print(root.right.val)
            else:
                insert(root.right,node)


def inorder(root): 
	if root: 
		inorder(root.left) 
		print(root.val) 
		inorder(root.right) 


r = Node(50) 
insert(r,Node(30)) 
insert(r,Node(20)) 
insert(r,Node(40)) 
insert(r,Node(70)) 
insert(r,Node(60)) 
insert(r,Node(80)) 


inorder(r)