import turtle

turtle.setup(400,500)    #setup window size
wn = turtle.Screen()     # Get reference to the window
wn.title("How to handle mouse clicks on the window!")
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("purple")
tess.pensize(3)
tess.shape("circle")


def h1(x,y):
    tess.goto(x,y)

wn.onclick(h1)    # Wire up a clock on the window
wn.mainloop()
