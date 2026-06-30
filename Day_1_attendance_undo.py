"""
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






        


