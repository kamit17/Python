import turtle
def draw_bar(t, height):
    """ Get turtle t to draw one bar , of height."""
    t.begin_fill()
    t.left(90)
    t.forward(height) # Draw up the left side
    t.write("  "+ str(height))
    t.right(90)
    t.forward(40) # width of bar , along the top
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
    t.penup()
    t.forward(10)   #leave small gap after each bar
    t.pendown()


wn = turtle.Screen()  # Setup the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle()  # create tess and set attributes
tess.color("blue","red")
tess.pensize(3)
tess.penup()
tess.backward(100)          # Position t at a convenient spot.
tess.pendown()


xs = [48,117,200,240,260,220]

for a in xs:
    draw_bar(tess,a)

wn.mainloop()