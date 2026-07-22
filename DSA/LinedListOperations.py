class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    # def __init__(self):
    #     self.head = None
    #     self.tmp = None

    head = None
    tmp = None

    def createLL(self,data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            self.tmp = newNode
            return
        
        self.tmp.next = newNode
        self.tmp = newNode
        return self.head

    
    def traverseLL(self,h):
        t1 = h
        while t1:
            print(t1.data,end="->")
            t1 = t1.next

    def copyll(self,head1):
        t1=head1
        head2 = None
        tmp2 = None

        
        while t1:
            newNode = Node(t1.data)

            if head2 is None:
                head2 = newNode
                tmp2 = newNode          
            else:
                tmp2.next = newNode
                tmp2 = newNode
            t1=t1.next

        print("Copied data:\n")
        self.traverseLL(head2)    

    def sortLL(self,head):
        t1 = head
        while t1:

            t2 = t1.next
            while t2:
                if t2.data < t1.data:
                    tmp = t2.data
                    t2.data = t1.data
                    t1.data = tmp
                t2 = t2.next
            t1 = t1.next

    

     

ll= LinkedList()
head=None
head2 = None

while True:
    ch=int(input("\n1=>create \n2=>traverse \n3=>Copy \n4=>Sorting \n0=>Exit \nEnter Your choice:"))
    
    if ch == 1:
        data=int(input("Enter Data:"))
        head=ll.createLL(data)
    elif ch == 2:
        ll.traverseLL(head)

    elif ch == 3:
        head2=ll.copyll(head)
    elif ch == 4:
        ll.sortLL(head)
    

    elif ch == 0:
        break

    else:
        print("\nInvalid Choice")



        
        