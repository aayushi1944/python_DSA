"""
H3) The GPS Navigation System (Backtracking)
You're building a GPS app like Google Maps for a hiking trail. The hiker moves through checkpoints. If they take a wrong tum, they hit "Go Back" to return to the previous checkpoint. But once they go back, they can also "Go Forward" if they change their mind again just like a browser's back/forward buttons

Operations:
visit(place)-move to a new place
back()- go to previous place
forward-go forward if available
"""


class GPSNavigation:

    def __init__(self):
        self.back_stack = []
        self.forward_stack = []
        self.current = None

    def visit(self, place):
        if self.current is not None:
            self.back_stack.append(self.current)

        self.current = place
        self.forward_stack.clear()
        print("Visited:", self.current)

    def back(self):
        if not self.back_stack:
            print("No previous location.")
            return

        self.forward_stack.append(self.current)
        self.current = self.back_stack.pop()
        print("Back to:", self.current)

    def forward(self):
        if not self.forward_stack:
            print("No forward location.")
            return

        self.back_stack.append(self.current)
        self.current = self.forward_stack.pop()
        print("Forward to:", self.current)

    def current_location(self):
        print("Current Location:", self.current)


gps = GPSNavigation()

# Static Input
gps.visit("Entrance")
gps.visit("Bridge")
gps.visit("Waterfall")
gps.visit("Hill Top")

gps.back()
gps.back()

gps.forward()

gps.visit("Forest")

gps.forward()   

gps.current_location()