class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyCircularLL:
    def __init__(self):
        self.head = None
        self.tmp = None

    def createLL(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tmp = newNode
            self.tmp.next = self.head
            print(data,"inerted")
            return
        newNode.next = self.head
        self.tmp.next = newNode
        self.tmp = newNode
        print(data,"inerted")

    def traverseLL(self):
        if self.head is None:
            print("Empty Linked list")
            return
        
        t1= self.head
        while True:
            print(t1.data, end="->")
            t1 = t1.next
            if t1 == self.head:
                break
            
        

    def insertFirst(self, data):
        if self.head is None:
            self.createLL(data)
            return

        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        self.tmp.next = self.head
        print(data,"inerted at First")

    def insertLast(self, data):
        if self.head is None:
            self.createLL(data)
            return
        newNode = Node(data)
        newNode.next = self.head
        self.tmp.next = newNode
        self.tmp = newNode
        print(data,"inerted at last")
    def insertAtPosition(self,pos,data):
        newNode = Node(data)
        t1 = self.head
        c=1
        if pos == 1:
            self.insertFirst(data)
            return
        while c < pos-1 and t1.next != self.head:
            t1 = t1.next
            c+=1
        if t1.next == self.head:
            print("Position out of range")
            return
        newNode.next = t1.next
        t1.next = newNode
        print(data,"inerted at",pos)

    def deleteFromFirst(self):
        if self.head is None:
            print("Empty Linked list")
            return
        if self.head.next == self.head:
            print(self.head.data,"Removed")
            self.head = None
            self.tmp = None
            return
        print(self.head.data,"Removed")
        self.head = self.head.next
        self.tmp.next = self.head

    def  deleteFromLast(self):
        if self.head is None:
            print("Empty Linked list")
            return
        t1 = self.head
        while t1.next != self.tmp:
            t1 = t1.next
        print(self.tmp.data,"is removed")
        t1.next = self.head
        self.tmp = t1

    def deleteFromPos(self, pos):
        if self.head is None:
            print("Empty Linked list")
            return
        if pos == 1:
            self.deleteFromFirst()
            return
        c=1
        t1= self.head

        while c < pos-1 and t1.next != self.head:
            c+=1
            t1 = t1.next
        if t1.next == self.head:
            print("position outof range...!")
            return
        if t1.next.next == self.head:
            self.deleteFromLast()
            return
        print(t1.next.data,"removed")
        t1.next = t1.next.next


        


cll = SinglyCircularLL()
while True:       
    ch = int(input("\n1=>create \n2=>traverse \n3=>insert first \n4=>insert last \n5=>insert at position \n6=>Delete First \n7=>Delete Last \n8=>Delete Position \n0=>Exit  \nEnter your choice:"))

    if ch == 1:
        data = int(input("Enter data:"))
        cll.createLL(data)
    elif ch == 2:
        cll.traverseLL()
    elif ch == 3:
        data = int(input("Enter data:"))
        cll.insertFirst(data)
    elif ch == 4:
        data = int(input("Enter data:"))
        cll.insertLast(data)
    elif ch == 5:
        pos = int(input("Enter Position:"))
        data = int(input("Enter data:"))
        cll.insertAtPosition(pos,data)
    elif ch==6:
        cll.deleteFromFirst()
    elif ch == 7:
        cll.deleteFromLast()
    elif ch == 8:
        pos = int(input("Enter Position:"))
        cll.deleteFromPos(pos)
    
    elif ch == 0:
        break
    else:
        print("\ninvalid choice...!")
        