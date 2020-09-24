#Add some new key bindings to the first sample program:

# Pressing keys R, G or B should change tess’ color to Red, Green or Blue.
# Pressing keys + or - should increase or decrease the width of tess’ pen. Ensure that the pen size stays between 1 and 20 (inclusive).
# Handle some other keys to change some attributes of tess, or attributes of the window, or to give her new behaviour that can be controlled from the keyboard.

import turtle

turtle.setup(400,500)                # Determine the window size
wn = turtle.Screen()                 # Get a reference to the window
wn.title("Handling keypresses!")     # Change the window title
wn.bgcolor("lightgreen")             # Set the background color
tess = turtle.Turtle()               # Create our favorite turtle

# The next four functions are our "event handlers".
def h1():
   tess.forward(30)

def h2():
   tess.left(45)

def h3():
   tess.right(45)

def tess_blue():
    tess.fillcolor("blue")

def tess_green():
    tess.fillcolor("green")

def tess_red():
    tess.fillcolor("red")

#Pressing keys + or - should increase or decrease the width of tess’ pen.

def tess_plus():
    if tess.pensize() <=19:
        tess.pensize(tess.pensize() + 1)
    #tess.pensize(tess.pensize() + 1)

def tess_minus():
    if tess.pensize() >= 2:
        tess.pensize(tess.pensize() -1)

def tess_shrink():
    """Make tess smaller."""
    temp = tess.shapesize()
    tess.shapesize(temp[0] * .9, temp[1] * .9, temp[2] * .9)
def tess_grow():
    """Make tess larger."""
    temp = tess.shapesize()
    tess.shapesize(temp[0] / .9, temp[1] / .9, temp[2] / .9)
def h4():
    wn.bye()                        # Close down the turtle window

# These lines "wire up" keypresses to the handlers we've defined.
wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Right")
wn.onkey(tess_blue,"b")
wn.onkey(tess_green,"g")
wn.onkey(tess_red,"r")
wn.onkey(tess_plus,"plus")
wn.onkey(tess_minus,"minus")
wn.onkey(tess_shrink, "s")
# Tess gets larger when d is pressed.
wn.onkey(tess_grow, "d")
wn.onkey(h4, "q")

# Now we need to tell the window to start listening for events,
# If any of the keys that we're monitoring is pressed, its
# handler will be called.
wn.listen()
wn.mainloop()


