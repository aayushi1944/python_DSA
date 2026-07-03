def multipliction(n1,n2):
    if n2==0:
        return 0 
    return n1 + multipliction(n1,n2-1)
    

print(multipliction(25,5))