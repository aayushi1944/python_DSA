"""
h2) Toll Plaza Simulation (Circular Queue)
A toll plaza has a fixed capacity of 5 vehicles. If full, new vehicles must wait Implement a Circular Queue to simulate this, since it reuses empty slots without wasting memory.
"""

class CircularQueue:

    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def enqueue(self, vehicle):
        if (self.rear + 1) % self.size == self.front:
            print(vehicle, "-> Queue is Full! Vehicle must wait.")
            return

        if self.front == -1:
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size

        self.queue[self.rear] = vehicle
        print(vehicle, "entered the toll plaza.")

    def dequeue(self):
        if self.front == -1:
            print("Queue is Empty!")
            return

        print(self.queue[self.front], "has crossed the toll.")

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

    def display(self):
        if self.front == -1:
            print("Queue is Empty!")
            return

        print("Vehicles in Queue:")

        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()

cq = CircularQueue(5)


cq.enqueue("Car")
cq.enqueue("Bus")
cq.enqueue("Truck")
cq.enqueue("Bike")
cq.enqueue("Van")

cq.display()

cq.enqueue("Auto")      

cq.dequeue()
cq.dequeue()

cq.display()

cq.enqueue("Auto")
cq.enqueue("Jeep")

cq.display()