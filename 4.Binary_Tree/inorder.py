class Node: 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None
def inorder(temp):
	current=temp
	stack=[]
	done=0
	while True:
		if current is not None:
			stack.append(current)
			current=current.left
		elif(stack):
			current=stack.pop()
			print(current.data,end="  ")
			current=current.right
		else:
			break
	print()

if __name__=='__main__':
	root=Node(10)
	root.left=Node(23)
	root.left.left=Node(24)
	root.right=Node(45)
	inorder(root)