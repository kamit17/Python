"""Exercise 10.6.5 from a textbook.

_How to Think Like a Computer Scientist: Learning with Python 3_
"""
import turtle


def draw_housing():
    """Draw a nice housing to hold the traffic lights."""
    tess.pensize(3)
    tess.color("black", "Dim Grey")
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

    States 0, 1, 2, 3 correspond to green, green+orange, orange, red
    in our modified traffic light system.
    """
    global state_num
    # Transition from 'green' to 'green plus orange'.
    if state_num == 0:
        orange_light.color("Orange")
        state_num = 1
        time_to_change = 1000
    # Transition from 'green plus orange' to 'orange'.
    elif state_num == 1:
        green_light.color("Dark Olive Green")
        state_num = 2
        time_to_change = 1000
    elif state_num == 2:     # Transition from 'orange' to 'red'
        orange_light.color("Sienna")
        red_light.color("red")
        state_num = 3
        time_to_change = 2000
    elif state_num == 3:       # Transition from 'red' to 'green'
        red_light.color("Brown")
        state_num = 0
        green_light.color("Lime Green")
        time_to_change = 3000
    else:
        print("Uh oh. Problem in the state machine.")

    wn.ontimer(advance_state_machine, time_to_change)


# Set up turtle and screen to work with.
# Tess will draw the housing, and
# turtles with obvious names will serve as lights.

# Set up tess.
turtle.setup(400, 500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()

# Draw the housing and move tess into position.
tess.penup()
tess.forward(-40)
tess.pendown()

draw_housing()
tess.penup()
tess.hideturtle()

# Set up tess's three counterparts.
green_light = turtle.Turtle()
orange_light = turtle.Turtle()
red_light = turtle.Turtle()

# Make them the appropriate colors and such
green_light.shape("circle")
orange_light.shape("circle")
red_light.shape("circle")

green_light.shapesize(3)
orange_light.shapesize(3)
red_light.shapesize(3)

green_light.fillcolor("Dark Olive Green")
orange_light.fillcolor("Sienna")
red_light.fillcolor("Brown")

# The three lights shouldn't draw anything, so
# let's preemptively stop them.
green_light.penup()
orange_light.penup()
red_light.penup()

# Turn them all to face upward.
green_light.left(90)
orange_light.left(90)
red_light.left(90)

# Walk them to their places
green_light.forward(50)
orange_light.forward(120)
red_light.forward(190)

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