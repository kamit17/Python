import turtle     # Tess becomes a traffic light.

turtle.setup(400,500)
wn = turtle.Screen()
wn.title('Tess becomes a traffic light')
wn.bgcolor('lightgreen')
tess = turtle.Turtle()


def draw_housing():
    """Draw a nice housing to hold the traffic lights"""
    tess.pensize(3)
    tess.color("black","darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(400,180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()


draw_housing()

tess.penup()
#Position tess onto the place where the greenlight should be
tess.forward(40)
tess.left(90)
tess.forward(50)
#Turn tess into a big green circle
tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")


wn.mainloop()
