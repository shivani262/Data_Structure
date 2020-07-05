def minidex(queue):
	min_index=-1
	min_value=9999999999
	for i in range(0,n):
		curr=queue[0]
		queue.get()		
		if (min_value>=curr):
			min_value=curr
		queue.append(min_value)