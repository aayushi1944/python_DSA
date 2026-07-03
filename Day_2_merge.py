"""
h3) Merge Sort - The IRCTC Waitlist Merger
IRCTC has two separately sorted waitlists one from its mobile app, one from railway counters. 
To produce a final unified waitlist, they don't re-sort from scratch. They merge both sorted lists in
 one pass compare the front of each list, pick the smaller token, advance. This is exactly merge sort's merge step.
"""

app=[3,9,27,38,38,38,38,43]
r_counter=[5,10,14,82]

def merge(arr1,arr2):
    s=[]
    i=0
    j=0
    while(i<=len(arr1)-1 and  j<=len(arr2)-1):
            if arr1[i] < arr2[j]:
                  s.append(arr1[i])
                  i=i+1
            else:
                  s.append(arr2[j])
                  j=j+1 
    if i < len(arr1):  
        while(i < len(arr1)):
            if arr1[i]:
                    s.append(arr1[i])
                    i=i+1
    if j < len(arr2): 
        while(j < len(arr2)):
            if arr2[j]:
                    s.append(arr2[j])
                    j=j+1                                  
    return s

print(merge(app,r_counter))
