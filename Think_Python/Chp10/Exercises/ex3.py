#In an earlier chapter we saw two turtle methods, hideturtle and showturtle that can hide or show a turtle. This suggests that we could take 
# a different approach to the traffic lights program. Add to your program above as follows: draw a second housing for another set of traffic 
# lights. Create three separate turtles to represent each of the green, orange and red lights, and position them appropriately within your 
# new housing. As your state changes occur, just make one of the three turtles visible at any time.


import turtle


def draw_housing():
    """Draw a nice housing to hold the traffic lights."""
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()


def advance_state_machine():
    """Move stoplight on to the next state.

    States 0, 1, 2 correspond to green, yellow, red
    in a standard traffic light.
    """
    global state_num
    if state_num == 0:       # Transition from state 0 to state 1
        green_light.hideturtle()
        tess.forward(70)
        yellow_light.showturtle()
        tess.fillcolor("orange")
        state_num = 1
    elif state_num == 1:     # Transition from state 1 to state 2
        yellow_light.hideturtle()
        tess.forward(70)
        red_light.showturtle()
        tess.fillcolor("red")
        state_num = 2
    elif state_num == 2:       # Transition from state 2 to state 3
        red_light.hideturtle()
        tess.back(140)
        tess.fillcolor("green")
        state_num = 0
        green_light.showturtle()
    else:
        print("Uh oh. Problem in the state machine.")

    wn.ontimer(advance_state_machine, 1000)


# Set up turtles and screen to work with.
# Tess will be the turtle who moves background
# and plays all three roles (red, green, yellow light)
# in the stoplight on the right. Three other turtles, with
# obvious names, will serve the left stoplight.

# Set up tess.
turtle.setup(400, 500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()

# Set up tess's three counterparts.
green_light = turtle.Turtle()
yellow_light = turtle.Turtle()
red_light = turtle.Turtle()

# Make them the appropriate colors and such
green_light.shape("circle")
yellow_light.shape("circle")
red_light.shape("circle")

green_light.shapesize(3)
yellow_light.shapesize(3)
red_light.shapesize(3)

green_light.fillcolor("green")
yellow_light.fillcolor("orange")
red_light.fillcolor("red")

# The three lights shouldn't draw anything, so
# let's preemptively stop them.
green_light.penup()
yellow_light.penup()
red_light.penup()

# Move them all back toward the left housing.
green_light.forward(-110)
yellow_light.forward(-110)
red_light.forward(-110)

# Turn them all to face upward.
green_light.left(90)
yellow_light.left(90)
red_light.left(90)

# Walk them to their places
green_light.forward(50)
yellow_light.forward(120)
red_light.forward(190)

# Draw the housings and move tess into position.
draw_housing()

tess.penup()
tess.forward(-150)
tess.pendown()

draw_housing()
tess.penup()
tess.forward(150)

tess.penup()
# Position tess onto the place where the green light should be
tess.forward(40)
tess.left(90)
tess.forward(50)
# Turn tess into a big green circle
tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")

# A traffic light is a kind of state machine with three states,
# Green, Orange, Red.  We number these states  0, 1, 2
# When the machine changes state, we change tess' position and
# her fillcolor.
# This variable holds the current state of the machine.
state_num = 0


# Bind the event handler to a timer.
wn.ontimer(advance_state_machine(), 1000)

wn.listen()                      # Listen for events
wn.mainloop()
