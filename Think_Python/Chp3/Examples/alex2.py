
import turtle
window = turtle.Screen()
window.bgcolor("lightgreen")  # set the window background color
window.title("Hello, Tess!")  # set the window title

tess = turtle.Turtle()
tess.color("blue")  # Tell tess to change her color
tess.pensize(3)     # Tell tess to set her pen width


tess.forward(50)
tess.left(120)
tess.forward(50)

turtle.mainloop()