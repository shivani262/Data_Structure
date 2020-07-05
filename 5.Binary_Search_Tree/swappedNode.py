def swapped(arr,n):
    s=[]
    temp=0
    q=[]
    for i in arr:
        while len(s)>0 and s[-1]>i:
            temp=s.pop()
            q.append(temp)
            break
        s.append(i)
    temp=q[0]
    for i in range(n-1,-1,-1):
        if arr[i] is q[1]:
            j=arr[i+1]
            arr[i+1]=q[0]
            
        if arr[i] is q[0]:
            arr[i]=j
        

arr=[3,4,15,6,7,8,5]
swapped(arr,len(arr))
for  i in range(len(arr)):
    print(arr[i])