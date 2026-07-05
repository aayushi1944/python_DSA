"""
H2) You're building a file size calculator like Windows Explorer's "Properties". 
A folder can contain files OR more folders. Calculate the total size of any folder recursively.
"""
data=[ {"fnm":"f1.txt", "size":20, "type":"file"},
      {"fnm":"f2.txt", "size":22, "type":"file"},
      {"fnm":"f3.txt", "type":"folder","files":[
          {"fnm":"f4.txt", "size":22, "type":"file"},
          {"fnm":"f5.txt", "size":30, "type":"file"},
          {"fnm":"f5.txt", "size":30, "type":"file"},
        ]},
        {"fnm":"f6.txt", "size":25, "type":"file"},     
]


def calcSize(ind,d,s):

    for i in range(ind,len(d)):
        # print(d[i]["type"])

        if d[i]["type"]=="folder":
            s=calcSize(0,d[i]["files"],s)
        else:
            s=s+d[i]["size"]
    return s

print(calcSize(0,data,0))




'''
s=0
for i in data:
    if i["type"]=="folder":
        for j in i["files"]:
            s=s+j["size"]
            #print(j["type"])
    else:
        s=s+i["size"]
        #print(i["type"])
print("total size=>",s)
'''
# def size(d,i):

#     if data[i]["type"]=="file":
#         return data[i]["size"]
#     else:
#         l=[]
#         for j in data[i]["files"]:
#             l.append(j["size"])
#         return sum(l)


          
        




    
    
        
            
        



