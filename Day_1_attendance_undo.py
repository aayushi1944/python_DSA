"""

h2) Toll Plaza Simulation (Circular Queue)
A toll plaza has a fixed capacity of 5 vehicles. If full, new vehicles must wait Implement a Circular Queue to simulate this, since it reuses empty slots without wasting memory.
H3) The GPS Navigation System (Backtracking)
You're building a GPS app like Google Maps for a hiking trail. The hiker moves through checkpoints. If they take a wrong tum, they hit "Go Back" to return to the previous checkpoint. But once they go back, they can also "Go Forward" if they change their mind again just like a browser's back/forward buttons

Operations:
visit(place)-move to a new place
back()- go to previous place
forward-go forward if available

Roll No. 1 Index 0
Roll No. 2 Index 1
Styles
Roll No. 30- Index 29
Since every student has a fixed slot (index), the teacher can directly go to any student's attendance without checking the previous records.
For example:
If the teacher wants to mark the attendance of Roll No. 16, they can directly access index 15.
There is no need to search from Roll No. 1 to Roll No. 16
This is called direct (random) access, which is the most important feature of an array

C2) The Undo Machine
You're building a lightweight text editor for a startup. Every time a user types a character, it gets recorded When they press Ctrl+Z 
(Undo) the last action must be reversed. The editor must support.
type(char)-records a character
. undo() removes the last typed character
getText()returns the current text

c3) The Smart Printer Queue (Priority Queue)
An office printer handles jobs in order, BUT jobs marked URGENT must be printed before normal jobs Design a system using two queues one for urgent, one for normal-and always drain urgent first
"""

def attendance():
    l=["AB"]*30
    l[16]="P"
    print(l)
#attendance()

class undoMachine:
    def __init__(self):
        self.stack=[]
    
    def type(self,ch):
        self.stack.append(ch)
    
    def undo(self):
        if self.stack:
            self.stack.pop()

    def getText(self):
        return ''.join(self.stack)

obj=undoMachine()

obj.type("A")
obj.type("a")
obj.type("y")
obj.type("u")
obj.type("s")
obj.type("h")
obj.type("i")

obj.undo()
print(obj.getText())






        


