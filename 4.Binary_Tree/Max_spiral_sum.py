class Node:
	def __init__(self,data):
		self.data=data
		self.right=None
		self.left=None

def maxSum(root):
	q=[]
	q.append(root)
	if root is None:
		return
	while(q):
		temp=q.pop()
		
		maxSum(temp.left)
		maxSum(temp.right)
		print(temp.data)

root = Node(-2) 
root.left = Node(-3) 
root.right = Node(4) 
root.left.left = Node(5) 
root.left.right = Node(1) 
root.right.left = Node(-2) 
root.right.right = Node(-1) 
root.left.left.left = Node(-3) 
root.right.right.right = Node(2) 
maxSum(root)