def interleave(high,low,s1,s2,queue,q):
	mid=int((high-low)/2)                    #for even no.
	for i in range(0,mid):
		s1.append(queue[i])
	for i in range(mid,n):
		s2.append(queue[i])
	while (len(s1)!=0 or len(s2)!=0):
		x=s2[-1]
		s2.pop()
		q.append(x)
		y=s1[-1]
		s1.pop()
		q.append(y)
def printq(q):
	for i in range(len(q)-1,-1,-1):
		print(q[i])

s1=[]
s2=[]
q=[]

queue=[11,12,13,14,15,16,17,18,19,20]
n=len(queue)
interleave(len(queue),0,s1,s2,queue,q)
printq(q)



		

	

	