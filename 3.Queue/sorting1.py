def min():
	min_index=-1
	min_value=9999999999
	for i in range(0,len(queue)):
		curr=queue[i]
		if (min_value>=curr):
			min_value=curr
			min_index=i
	return min_index
def sorting(queue,n,s):
	while n!=0:
		i=min()
		x=queue[i]
		del queue[i]
		s.append(x)
		n-=1

	
def printq(s):
	for i in range(0,len(s)):
		print(s[i])

queue=[3,1,6,4,8,9,18]
s=[]
n=len(queue)
sorting(queue,n,s)
printq(s)
