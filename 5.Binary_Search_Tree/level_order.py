INT_MAX , INT_MIN = 50,-50
class Node:
    def __init__(self,data,min,max):
        self.data=data
        self.min=min
        self.max=max
def levelorder(arr,n):
    q=[]
    i=0
    newnode=Node(arr[i],INT_MIN,INT_MAX)
    i+=1
    q.append(newnode)
    print(q.pop())
    


arr=[7, 4, 12, 3, 6, 8, 1, 5, 10]
n=len(arr)
if (levelorder(arr,n)):
    print("yes")
else:
    print("no")














