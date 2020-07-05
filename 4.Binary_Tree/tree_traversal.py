class Node:
	def __init__(s,data):
		s.data=data
		s.left=None
		s.right=None
def inorder(root):
	if root :
		inorder(root.left)
		print(root.data, end=" ")
		inorder(root.right)

def preorder(root):
	if root :
		print(root.data, end=" ")
		preorder(root.left)
		preorder(root.right)
def postorder(root):
	if root :
		postorder(root.left)
		postorder(root.right)
		print(root.data, end=" ")

root=Node(21)
root.left=Node(24)
root.right=Node(25)
root.left.left=Node(26)
root.right.left=Node(27)
root.left.right=Node(28)
root.right.right=Node(29)
inorder(root)
print()
preorder(root)
print()
postorder(root)
print()