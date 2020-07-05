class newNode:
	def __init__(self,data):
		self.data=data
		self.right=None
		self.left=None

def kpath(root,s,key):
	if not root:
		return
	
	kpath(root.left,s,key)
	
	kpath(root.right,s,key)
	s.append(root.data)
	f=0
	for j in range(len(s)-1,-1,-1):
		f=f+s[j]
		if f==key:
			printq(s,j)
def printq(s,j):
	for i in range(j,len(s)):
		print(s[i], end=" ")
	print()


root = newNode(1)  
root.left = newNode(3)  
root.left.left = newNode(2)  
root.left.right = newNode(1)  
root.left.right.left = newNode(1)
root.right = newNode(-1) 
root.right.left = newNode(4)  
root.right.left.left = newNode(1)  
root.right.left.right = newNode(2)  
root.right.right = newNode(5)  
root.right.right.right = newNode(2) 
s=[]
kpath(root,s,5)
 