import turtle
window = turtle.Screen()    # Set up the window and its attributes
window.bgcolor("orange")
window.title('Tess & Alex')


tess = turtle.Turtle()   # Creaet tess and set some attributes
tess.color("hotpink")
tess.pensize(5)

alex = turtle.Turtle()  # Create Ales

tess.forward(80)        # Make tess draw equilateral triangle
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)

tess.right(180)  # Turn tess around
tess.forward(80)  # Move her away from the origin

alex.forward(50)  # Make alex draw a square
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)


window.mainloop()
