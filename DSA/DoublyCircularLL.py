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

dLL = DoublyCircular()
while True:

    ch=int(input("\n1=>create \n2=>traverse \n3=>insert first \n4=>insert last \n5=>insert at position \n6=>Delete First \n7=>Delete Last \n8=>Delete Position \n0=>Exit  \nEnter your choice:"))
    if ch ==1:
        data = int(input("Enter data"))
        dLL.createLL(data)
    elif ch == 2:
        dLL.traverse()

    elif ch == 0:
        break
    else:
        print("invalid choce...!")





        