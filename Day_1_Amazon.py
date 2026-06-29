"""
H1) An Amazon fulfilment centre has a conveyor belt with exactly 8 slots numbered 0-7. Each slot holds one product. 
The warehouse manager needs to: check what's at a slot, find a product, update a slot, and check if the belt is full. 
The conveyor belt - fixed 8 slots
"""
class amazon:
    def __init__(self):
        self.belt=["mobile","laptop","head phones","shirt","t-shirt","Bluetooth ","speaker","Temperature Sensor"]
    
    def whatsAtSlot(self,i):
        return self.belt[i]
    
    def isAvailable(self,nm):
        if nm in self.belt:
            return 1,self.belt.index(nm)
        else:
            return(0,)
        
    def updateSlot(self,ind,nm):
        self.belt[ind]=nm
        print(self.belt)
    
    def  isFull(self):
        if None not in self.belt:
            print("self is Full")
        else:
            print("self is not full")
    

    
obj = amazon()

ind=int(input("Enter index[0-7]:"))
print(ind ,": ",obj.whatsAtSlot(ind))


nm=input("Enter Product name:")
if obj.isAvailable(nm)[0]:
    print("Product find at",obj.isAvailable(nm)[1]," position")
else:
    print("not found")    
        
i=int(input("Enter slot you want to update[0-7]:"))
prd=input("Enter new  product:")
obj.updateSlot(i,prd)

obj.isFull()