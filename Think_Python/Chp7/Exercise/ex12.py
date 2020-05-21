# Many interesting shapes can be drawn by the turtle by giving a list of pairs like we did above,
# where the first item of the pair is the angle to turn, and the second item is the distance to move forward.
# Set up a list of pairs so that the turtle draws a house with a cross through the centre, as show here.
# This should be done without going over any of the lines / edges more than once, and without lifting your pen.

import turtle

def travel(ttl,turns_and_steps):
    """Takes a turtle ttl and specifically formatted list of turns_and_steps, and causes the turtle to trace out lines dtermined by  the turns and steps."""
    for x in turns_and_steps:
        ttl.left(x[0])
        ttl.forward(x[1])


wn = turtle.Screen()
tess = turtle.Turtle()

s = 100      # sets a scale of drawings
turns_and_steps = [(180,s),
                   (-135,s * 2 **0.5),
                   (135,s),
                   (135,s*2**0.5),
                   (135,s),
                   (45,s*.5**0.5),
                   (90,s*.5**0.5),
                   (45,s)]
travel(tess,turns_and_steps)

wn.mainloop()


