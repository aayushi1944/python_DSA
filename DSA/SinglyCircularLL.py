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
            return
        newNode.next = self.head
        self.tmp.next = newNode
        self.tmp = newNode

    def traverseLL(self):
        t1= self.head
        while t1.next != self.head:
            print(t1.data, end="->")
            t1 = t1.next
        print(t1.data)

    def insertFirst(self, data):

        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        self.tmp.next = self.head

    def insertLast(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.tmp.next = newNode
        self.tmp = newNode
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

    def deleteFromFirst(self):
        self.head = self.head.next
        self.tmp = self.head

        


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
    
    
    elif ch == 0:
        break
    else:
        print("\ninvalid choice...!")
        