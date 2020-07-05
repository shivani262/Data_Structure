class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
def preorder(root,q):
    if root is None:
        return
    preorder(root.left,q)
    q.append(root.data)
    preorder(root.right,q)
def small(k,q):
    print(q[k-1])
q=[]
root=Node(30)
root.left=Node(25)
root.right=Node(35)
root.left.left=Node(22)
root.left.right=Node(27)
preorder(root,q)
small(2,q)
