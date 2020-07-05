def reverseQueue(q): 

	
	if (len(q)==0): 
		return

	data = q[0]; 
	q.pop(0)
	reverseQueue(q) 

	q.append(data) 
def printq(q):
	for i in range(0,len(q)):
		print(q[i])
q=[1,2,3,4,5,6,7,8]
reverseQueue(q)
printq(q)
