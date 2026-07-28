class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyCircular:
    def __init__(self):
        self.head = None
        self.tail = None

    def createLL(self,data):
        newNode = Node(data)
        print(data , "inserted")
        if self.head is None:
            newNode.next = newNode
            newNode.prev = newNode
            self.head = self.tail = newNode            
            return
        newNode.next = self.head
        newNode.prev = self.tail
        self.tail.next = newNode
        self.tail = newNode
        self.head.prev = self.tail

    def traverse(self):
        t1 = self.head
        if self.head is None:
            print("list is empty")
            return
        while t1.next != self.head:
            print(t1.data,end="->")
            t1 = t1.next
        print(t1.data)

    def insertFirst(self,data):
        if self.head is None:
            self.createLL(data)
            return
        newNode = Node(data)
        newNode.next = self.head
        newNode.prev = self.tail
        newNode.next.prev = newNode
        self.head = newNode
        self.tail.next = newNode
        print(data,"inserted at  first")

    def insertLast(self,data):
        if self.head is None:
            self.createLL(data)            
            return

        newNode = Node(data)
        newNode.prev = self.tail
        newNode.next = self.head
        self.tail.next = newNode
        self.tail = newNode
        print(data,"inserted at last")

    def insertPosition(self, data, pos):
        c = 1
        newNode = Node(data)
        t1 = self.head

        if pos == 1:
            self.insertFirst(data)
            return
        while c<pos-1 and t1.next != self.head:
            c+=1
            t1 = t1.next
        if t1.next == self.head:
            print("Position Out of range")
            return
        newNode.next = t1.next
        newNode.prev = t1
        t1.next.prev = newNode
        t1.next = newNode
        print(data,"inserted at",pos)

    def deleteFirst(self):
        if self.head is None:
            print("Empty linked list")
            return
        if self.head.next == self.head:
            print(self.head.data,"removed")
            self.head = self.tail = None
            return
        print(self.head.data,"removed")
        self.head.next.prev = self.tail
        self.head = self.head.next
        self.tail.next = self.head

    def deleteLast(self):
        if self.head is None:
            print("Empty linked list")
            return
        if self.head.next == self.head:
            print(self.head.data,"removed")
            self.head = self.tail = None
            return
        print(self.tail.data,"removed")
        self.tail.prev.next = self.head
        self.tail = self.tail.prev
        self.head.prev = self.tail

    def deleteAtPosition(self,pos):
        c = 1
        t1 = self.head
        if pos == 1:
            self.deleteFirst()
            return
        while c<pos-1 and t1.next != self.head:
            c+=1
            t1 = t1.next
        if t1.next == self.head:
            print("Position Out of range")
            return
        if t1.next.next == self.head:
            self.deleteLast()
            return
        print(t1.next.data,"removed")
        t1.next = t1.next.next
        t1.next.prev = t1

        



dLL = DoublyCircular()
while True:

    ch=int(input("\n1=>create \n2=>traverse \n3=>insert first \n4=>insert last \n5=>insert at position \n6=>Delete First \n7=>Delete Last \n8=>Delete Position \n0=>Exit  \nEnter your choice:"))
    if ch ==1:
        data = int(input("Enter data"))
        dLL.createLL(data)
    elif ch == 2:
        dLL.traverse()
    elif ch == 3:
        data = int(input("Enter data"))
        dLL.insertFirst(data)
    elif ch ==4:
        data = int(input("Enter data"))
        dLL.insertLast(data)
    elif ch == 5:
        pos = int(input("Enter Position:"))
        data = int(input("Enter data:"))
        dLL.insertPosition(data, pos)
    elif ch == 6:
        dLL.deleteFirst()
    elif ch == 7:
            dLL.deleteLast()
    elif ch == 8:
            pos = int(input("Enter Position:"))
            dLL.deleteAtPosition(pos)
    elif ch == 0:
        break
    else:
        print("invalid choce...!")





        