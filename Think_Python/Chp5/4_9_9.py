# This is the same as ex9 but took it from Mitchell B powell.
# THis program divides the program into 3 functions . One to set the caption
# One for color and one for the draw function .
def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. Fills bar with color 
        as specified in _How to Think Like a Computer Scientist: 
        Learning with Python 3_, chapter 5, exercise 14.8."""

    set_fill_color(t, height)

    t.begin_fill()             # Turn fill on before drawing.
    t.left(90)                 # Turn to face upward
    t.forward(height)          # Draw line upward (if height is positive)
    height_caption(t, height) # Write height caption for our bar
    t.right(90)             # Turn to produce "top" (for positive values).
    t.forward(40)           # Draw the "top".
    t.right(90)             # Turn to draw other side of bar.
    t.forward(height)       # Draw other side of bar.
    t.left(90)              # Turn back to original position.
    t.end_fill()            # Fill in the bar.
    t.penup()               # Stop drawing.
    t.forward(10)           # Move into position for the next bar.
    t.pendown()             # And get ready to draw again.

def height_caption(t, height):
    """When called at the right time, this writes a caption for our 
       bar, displaying its height. If the bar represents a positive number, it 
       writes the caption above the bar. For a negative number, below the bar."""

    if height <0:                      # If height is negative, 
        t.penup()                      # we pick up pen to stop drawing for a bit,
        t.backward(17)                 # move downward to an appropriate spot,
        t.write("  "+ str(height))     # write our caption, 
        t.forward(17)                  # move back up to resume,
        t.pendown()                    # and put our pen back down to continue.
    else:                              # Otherwise, height is positive, and 
        t.write("  "+ str(height))     # we can just go ahead and caption.

def set_fill_color(t, height):
    """Sets fill-color of a turtle based on the scheme
       laid out in exercise 5.14.9 of _How to Think Like a Computer
       Scientist: Learning with Python 3_"""

    if height >= 200:
        t.color("blue", "red")
    elif height >= 100:
        t.color("blue", "yellow")
    elif height < 100:
        t.color("blue", "green")


import turtle

wn = turtle.Screen()         # Set up the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle()       # Create a turtle and set some attributes
tess.color("blue", "red")
tess.pensize(3)

xs = [48,117,200,-240,160,-260,220]      # Our data to graph

for a in xs:                            # Graph the bars in order.
    draw_bar(tess, a)

wn.mainloop()                           # Hold screen open till user is done.