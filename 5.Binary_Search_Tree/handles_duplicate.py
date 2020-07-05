class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.count=1
def Handle(root,key):
    if root is None:
        node=Node(key)
        return node
    if root.data==key:
        root.count+=1
        return root
    if root.data > key:
        root.left=Handle(root.left,key)
    else:

        root.right=Handle(root.right,key)
        
    return root
def inorder(root):
    if root is None:
        return
    else:
        inorder(root.left)
        print(root.data,root.count)
        inorder(root.right)
root =None
root=Handle(root,10)
root=Handle(root,30)
root=Handle(root,30)
root=Handle(root,40)
root=Handle(root,30)
root=Handle(root,60)
root=Handle(root,70)
root=Handle(root,80)
root=Handle(root,90)
root=Handle(root,10)

inorder(root)