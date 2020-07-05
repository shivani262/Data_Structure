min=-50
max=50
class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
def BinarySearch(root,min,max):
    if root is None:
        return True
    if (root.data<min or root.data>max):
        return False
    return (BinarySearch(root.left,min,root.data-1) and BinarySearch(root.right,root.data+1,max))

root = Node(9) 
root.left = Node(2) 
root.right = Node(5) 
root.left.left = Node(1) 
root.left.right = Node(3) 
if BinarySearch(root,min,max):
    print("yes")
else:
    print("no")

