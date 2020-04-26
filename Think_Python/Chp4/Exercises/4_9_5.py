def square_spiral(ttl, trn, fwd):
    """Make turtle ttl draw a blue 'square spiral', 
       turning trn degrees at each corner. Before drawing
       it moves forward fwd (backward if fwd is negative)."""

    ttl.color("blue")    # Set up turtle's attributes
    ttl.pensize(1.5)
    ttl.speed(10)

    ttl.penup()          # Move to starting position.
    ttl.forward(fwd)

    ttl.pendown()           # Draw the spiral.
    for a in range(0, 100):
        ttl.forward(a * 2)
        ttl.right(trn)

import turtle

wn = turtle.Screen()        # Set up screen to draw on.
wn.bgcolor("lightgreen")
wn.title("Two spirals")

tess = turtle.Turtle()          # Make a turtle
square_spiral(tess, 90, -150)   # Draw the 'squarer' spiral

alex = turtle.Turtle()          # Another turtle        
square_spiral(alex, 89, 150)    # The 'slanted' spiral  

wn.mainloop()   # Hold screen open till user closes it.