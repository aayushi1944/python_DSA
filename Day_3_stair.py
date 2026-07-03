
def stair(n):
    if n==1 or n==2:
        return n
    return stair(n-1)+ stair(n-2)
print(stair(5))

