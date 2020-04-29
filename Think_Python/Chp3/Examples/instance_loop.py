import turtle
window = turtle.Screen()    # Set up the window and its attributes
window.bgcolor("orange")
window.title('Tess & Alex')


tess = turtle.Turtle()   # Creaet tess and set some attributes
tess.color("hotpink")
tess.pensize(5)
"""
for i in range(3):
    tess.forward(80)
    tess.left(120)

tess.right(180)
tess.forward(80)
"""

alex = turtle.Turtle()  # Create Alex
colors = ["yellow","red","purple","blue"]
for color in colors:
    alex.color(color)
    alex.forward(50)
    alex.left(90)

"""for i in range(4):
    alex.forward(50)
    alex.left(90)
"""   
window.mainloop()
