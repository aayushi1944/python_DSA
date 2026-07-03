"""
h2) The E-Commerce Price Filter (First occurrence 2 target)

You're on Flipkart. You filter products: "Show me laptops priced 50,000 or above." Products are sorted by price. Flipkart must find 
the first product ≥ 50,000- classic binary search variant called lower bound.

"""

l=[20000,30000,44000,48000,50000,50000,52000,55000]

def binSearch(p):
    s=0
    e=len(l)-1
    f=0   
    while(s <= e):
        mid=(s+e)//2
        if l[mid]==p:
            f=1
            print("found at ",mid)
            break
        elif p > l[mid]:
            s=mid+1 
        else:
            e=mid-1
    if f==0:
        print("not  found")


binSearch(20000)
    
    