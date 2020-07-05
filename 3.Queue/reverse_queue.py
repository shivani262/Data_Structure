def reverse(queue,s):
	
	while len(queue)!=0:
		x=queue[-1]
		queue.pop()
		s.append(x)
	
def printqueue(s):
	for i in range(0,len(s)):
		print(s[i])

#driver code
s=[]
queue=[1,4,7,8,9,3,4,7]
reverse(queue,s)
printqueue(s)

		
