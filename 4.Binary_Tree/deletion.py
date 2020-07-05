class Node:

	def __init__(self,data):
		self.data=data 
		self.left=None
		self.right=None
		
def inorder(temp,q):
	
	if (not temp):
		return
	inorder(temp.left,q)
	q.append(temp.data)
	print(temp.data,end=" ")
	inorder(temp.right,q)
	
def printq(q,key):
	temp=q[len(q)-1]
	for i in range(len(q)):
		if(q[i]==key):
			q[i]=temp
			q.pop()
			break
					
	for i in range(len(q)):
		print(q[i],end=" ")
	
	
	
if __name__=='__main__':
	q=[]
	root=Node(10)
	root.left=Node(12)
	root.right=Node(14)
	root.left.right=Node(17)
	root.left.left=Node(79)
	root.right.left=Node(23)
	root.right.right=Node(43)
	inorder(root,q)
	print()
	printq(q,43)
	