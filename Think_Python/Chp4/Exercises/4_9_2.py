"""Use a turtle to create a concentric arrangement of squares"""

def draw_square(ttl, len):
    """Takes a turtle ttl and uses it to create a square
    of sides len long."""

    ttl.pendown()          # Makes sure the turtle is ready to draw.
    for _ in range(4):
        ttl.forward(len)
        ttl.left(90)
    ttl.penup()             # Position turtle for next square
    ttl.backward(10)
    ttl.right(90)
    ttl.forward(10)
    ttl.left(90)

import turtle
window = turtle.Screen()            # Set up a window and some attributes
window.bgcolor("lightgreen")

alex = turtle.Turtle()              # Set up a turtle and some attributes
alex.color("HotPink")
alex.pensize(3)

for i in range(5):
    draw_square(alex, 20 + 20 * i)

window.mainloop()