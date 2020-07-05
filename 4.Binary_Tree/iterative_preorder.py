class Node:
	def __init__(self,data):
		self.data=data
		self.right=None
		self.left=None
def iterativePreorder(root):
	if (root is None):
		return
	s=[]
	s.append(root)
	while(len(s)>0):
		p=s.pop()
		print(p.data )
		if p.right is not None:
			s.append(p.right)
		if p.left is not None:
			s.append(p.left)

root=Node(10)
root.left=Node(11)
root.right=Node(12)
root.left.left=Node(13)
root.right.left=Node(14)
root.left.right=Node(15)
root.right.left=Node(16)
iterativePreorder(root)
