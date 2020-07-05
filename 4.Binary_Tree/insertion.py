class Node:
	def __init__(self,value):
		self.right=None
		self.left=None
		self.key=value
def inorder(temp):
	if (not temp):
		return
	inorder(temp.left)
	print(temp.key,end=" ")
	inorder(temp.right)
def insert(temp,key,q):
	q.append(temp)
	while (len(q)):
		temp=q[0]
		q.pop(0)
	
	if (not temp.left):
		temp.left=Node(key)
				
	else:
		q.append(temp.left)
			
	if (not temp.right):
		temp.right=Node(key)
				
	else:
		q.append(temp.right)
if __name__=="__main__":
	q=[]
	root = Node(10) 
	root.left = Node(11) 
	root.left.left = Node(7) 
	root.right = Node(9) 
	root.right.left = Node(15) 
	root.right.right = Node(8) 
	print("Inorder traversal before insertion:", end = " ") 
	inorder(root) 
	insert(root, 12,q) 
	print("Inorder traversal after insertion:", end = " ") 
	inorder(root)
		