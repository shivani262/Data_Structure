class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
def large(root,min,max):
    if root is None:
        return True
    if (root.data<min or root.data>max):
        temp=root.data
        print(count1(root,0))
         
       #return(large(root.left,min,root.data-1) or large(root.right,root.data+1,max))
    return(large(root.left,min,root.data-1) and large(root.right,root.data+1,max))

def count1(root,count):
    if root is None:
        return count
    if root.left is not None:
        count+=1
        return(count1(root.left,count))
    if root.right is not None:
        count+=1
        return(count1(root.right,count))
    return count


    
min=-1000
max=5000
root = Node(68)  
root.left = Node(65)      
root.right = Node(70)  
root.left.left = Node(50)
large(root , min ,max)

