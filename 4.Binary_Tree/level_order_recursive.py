class Node:
	def __init__(self,data):
		self.data=data
		self.right=None
		self.left=None
def height(root):
	if root is None:
		return 0
	else:
		lh=height(root.left)
		rh=height(root.right)
		if lh > rh:
			return lh+1
		else:
			return rh+1
def printlevel(root,h):
	
	if root is None:
		return	
	if h==1 :
		print(root.data)
	if h > 1 :
		printlevel(root.left,h-1)
		printlevel(root.right,h-1)
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
h=height(root)

for i in range(1,h+1):
	printlevel(root,i)
