# In the turtle bar chart program, what do you expect to happen if one or more of
# the data values in the list is negative? Try it out. Change the program so that
# when it prints the text value for the negative bars, it puts the text below the
# bottom of the bar.

import turtle
def draw_bar(t, height):
    """ Get turtle t to draw one bar , of height."""
    if height >=200:
        t.color("red")
    elif height>=100:
        t.color("yellow")
    else:
        t.color("green")
    t.begin_fill()
    t.left(90)
    t.forward(height) # Draw up the left side
    # Write caption for our bar
    if height <0:                      # If height is negative, 
        t.penup()                      # we pick up pen to stop drawing for a bit,
        t.backward(17)                 # move downward to an appropriate spot,
        t.write("  "+ str(height))     # write our caption, 
        t.forward(17)                  # move back up to resume,
        t.pendown()                    # and put our pen back down to continue.
    else:                              # Otherwise, height is positive, and 
        t.write("  "+ str(height))     # we can just go ahead and caption.
    #t.write("  "+ str(height))
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


xs = [48,117,200,199,240,260,220,-33]

for a in xs:
    draw_bar(tess,a)

wn.mainloop()
