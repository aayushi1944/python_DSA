l=[1,4,6,9,11,15,20]
def binSearch(val,d,s,e):
   
    if s > e:
        return -1
    mid=(s+e)//2
    if d[mid]==val:
        return mid
    elif d[mid] < val:
        return binSearch(val,d,mid+1,e) 
    else:
        return binSearch(val,d,s,mid-1) 

no=int(input("Enter value:"))  
if (binSearch(no,l,0,len(l)-1)) != -1:
    print("found")
else:
    print("not found")