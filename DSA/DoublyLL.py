class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLL:
    # head = None
    # tail = None
    
    def createLL(self,data, head, tail):
        newNode = Node(data)
        if head is None:
            head = newNode
            tail = newNode
            return head, tail
        newNode.prev = tail
        tail.next = newNode
        tail = newNode
        return head,tail
   


    def traversLL(self,head):
        t1=head
        while t1:
            print(t1.data,end="->")
            t1 = t1.next
    def backtraverse(self , tail):
        t1=tail
        while t1:
            print(t1.data,end="->")
            t1 = t1.prev

    def insertFirst(self, data, head , tail):
        newNode = Node(data)
        if head == None and tail == None:
            head = newNode
            tail = newNode
        else:
            newNode.next = head
            head.prev = newNode
            head = newNode
        return head , tail

    def insertLast(self ,data, tail,head):
        if tail is None:
            return self.createLL(data,head,tail)
        else:
            newNode = Node(data)
            tail.next = newNode
            newNode.prev = tail
            tail = newNode
            return head,tail

    def insertAtPosition(self, data,pos, head):
        newNode = Node(data)
        
        if pos == 1:
            return self.insertFirst(data,head)
            
        t1 = head
        c = 1
        while c < pos-1 and t1.next is not None :
            t1 = t1.next
            c+=1
        if t1.next is None:
            print("position out of range...!")
            return head
        newNode.next = t1.next
        newNode.prev = t1
        t1.next.prev = newNode
        t1.next = newNode
        return head
    
    def delFirst(self, head, tail):
        if head == None:
            print("Empty Linked List")
        elif head.next == None:
            head = None  
            tail = None    
        else:
            head.next.prev = None
            head = head.next
           
        return head, tail

    def delLast(self,head,tail):
        if tail is None:
            print("Empty Linked List")
            return head , tail
        if head == tail:
            print(tail.data,"removed")
            return None,None
        print(tail.data,"removed")
        t1= tail
        tail = tail.prev
        tail.next = None
        t1.prev = None

        return head, tail
       
        


dll = DoublyLL()
head = None
tail = None
while True:
    ch=int(input("\n1=>create \n2=>traverse  \n22=>Backtraverse  \n3=>insert first \n4=>insert last \n5=>insert at position \n6=>Delete First \n7=>Delete Last \n8=>Delete Position \n0=>Exit  \nEnter your choice:"))
    if ch == 1:
        data = int(input("Enter data:"))
        head , tail = dll.createLL(data, head, tail)
                
    elif ch == 2:
        dll.traversLL(head)
    elif ch == 22:
        dll.backtraverse(tail)

    elif ch == 3:
        data = int(input("Enter data:"))
        head, tail = dll.insertFirst(data,head,tail)

    elif ch == 4:
        data = int(input("Enter data:"))
        head,tail = dll.insertLast(data,tail,head)
    elif ch == 5:
        data = int(input("Enter data:"))
        pos = int(input("Enter Position:"))
        head=dll.insertAtPosition(data,pos,head)
    elif ch == 6:
        head, tail = dll.delFirst(head, tail)
    elif ch == 7:
        head,tail = dll.delLast(head,tail)


    elif ch == 0:
        break
    else:
        print("invalid choice...!")
        

