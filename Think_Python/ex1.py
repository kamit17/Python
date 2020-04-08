
"""
import turtle
bg_color = input('What is the background color?')
window = turtle.Screen()
window.bgcolor(bg_color)  # set the window background color
window.title("Hello, Tess!")  # set the window title

tess = turtle.Turtle()
tess.color("blue")  # Tell tess to change her color
tess.pensize(3)     # Tell tess to set her pen width


tess.forward(50)
tess.left(120)
tess.forward(50)

turtle.mainloop()

"""

import turtle

windowcolor = input("window color: ")
tesscolor = input("tess color: ")

# Set up window

window = turtle.Screen()
window.bgcolor(windowcolor)
window.title("Hello, Tess!")

# Set up turtle

tess = turtle.Turtle()
tess.color(tesscolor)
tess.pensize(3)

# Draw things

tess.forward(50)
tess.left(120)
tess.forward(50)

# Enter window loop

window.mainloop()