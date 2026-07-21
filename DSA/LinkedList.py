class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.temp = None


    def creatNode(self,data):
        newNode= Node(data)

        if self.head == None:
            self.head = newNode
            self.temp = newNode
            return
        
        self.temp.next = newNode
        self.temp = newNode
             
        # while self.temp.next:
        #     self.temp= self.temp.next
        # self.temp.next = newNode

    def insertFirst(self,data):
        newNode  = Node(data)

        if self.head == None:
            self.head = newNode
            self.temp = newNode
            return
        newNode.next = self.head
        self.head = newNode

    def insertLast(self,data):
        newNode = Node(data)

        if self.head == None:
            self.head = newNode
            self.temp = newNode
            return
        self.temp.next = newNode
        self.temp = newNode

    def insertPosition(self , data,pos):
        newNode = Node(data)
        if pos == 1:
            self.insertFirst(data)
            return
        c=1
        tmp = self.head
        while c < pos-1 and tmp.next is not None:
            tmp = tmp.next
            c+=1
        if tmp.next is None:
            print("Position out of range")
            return
        newNode.next = tmp.next
        tmp.next = newNode
    
    def deleteFirst(self):
        








    
    def traverse(self):
        if self.head == None:
            print("linked list is empty")
            return
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("None")



# ll=LinkedList()

# ll.creatNode(10)
# ll.creatNode(20)
# ll.creatNode(30)
# ll.creatNode(40)
# ll.creatNode(50)

# ll.traverse()

ll=LinkedList()
while True:

    ch=int(input("\n1=>create \n2=>traverse \n3=>insert first \n4=>insert last \n5=>insert at position \n6=>Delete First \n7=>Delete Last \n8=>Delete Position \n0=>Exit  \nEnter your choice:"))
    
    if ch == 1:
        
        data=int(input("Enter Data:"))        
        ll.creatNode(data)
    elif ch == 2:
        ll.traverse()
    elif ch ==3:
        data=int(input("Enter Data:"))      
        ll.insertFirst(data)
    elif ch == 4:
        data=int(input("Enter Data:"))      
        ll.insertLast(data)
    elif ch == 5:
        pos=int(input("Enter Position:"))  
        data=int(input("Enter Data:"))  
        ll.insertPosition(data,pos)



    elif ch==0:
        break
    else:
        print("invalid choice")
    
    
    
    

