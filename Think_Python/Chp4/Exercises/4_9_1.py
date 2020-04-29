"""
Write a void (non-fruitful) function to draw a square. Use it in a program to draw
the image shown below. Assume each side is 20 units. (Hint: notice that the turtle
has already moved away from the ending point of the last square when the program
ends.)

"""
import turtle
def draw_square(nm):
    """Takes a turtle (nm), draws a square with it, and then
    moves the turtle to the right."""
    for _ in range(4):
        nm.forward(20)
        nm.left(90)

    nm.penup()
    nm.forward(40)
    nm.pendown()

 

alex = turtle.Turtle()
alex.color("HotPink")
alex.pensize(3)
wn = turtle.Screen()
wn.bgcolor("lightgreen")

for dummy in range(5):
    draw_square(alex)

wn.mainloop()