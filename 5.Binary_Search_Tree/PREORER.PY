INT_MIN = -2**32
class Node:
    def __init__(self,data,min):
        self.data=data
        self.min=min
def preorder(arr,n):
    s=[]
    root=INT_MIN
    for i in arr:
        if i<root:
            return False
    
        while len(s)>0 and s[-1]<i:
            root=s.pop()
            print(root)
        s.append(i)
    
    return True



arr=[40,30,20,35,45,42,46]
n=len(arr)
if (preorder(arr,n)):
    print("yes")
else:
    print("no")