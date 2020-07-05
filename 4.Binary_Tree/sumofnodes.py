class newNode:  
  
    def __init__(self, key):  
        self.key = key 
        self.left = None
        self.right = None

def sums(root):
	if root is not None:
		return(root.key+sums(root.left)+sums(root.right))
	else:
		return 0


root = newNode(1)  
root.left = newNode(2)  
root.right = newNode(3)  
root.left.left = newNode(4)  
root.left.right = newNode(5)  
root.right.left = newNode(6)  
root.right.right = newNode(7)  
root.right.left.right = newNode(8)
s=sums(root)
print(s)