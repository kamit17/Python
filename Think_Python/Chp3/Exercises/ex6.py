"""
A drunk pirate makes a random turn and then takes 100 steps forward,makes another random turn,
takes another 100 steps, turns another random amount, etc. A social science student records the
angle of each turn before the next 100 steps are taken. Her experimental data is
[160, -43, 270, -97, -43, 200, -940, 17, -86]. (Positive angles are counter-clockwise.) Use a
turtle to draw the path taken by our drunk friend.

"""

import turtle   #Allows us to use turtles
wn = turtle.Screen() # creates a playground for turtles
alex = turtle.Turtle() # Create a turtle, assign to alex
alex.shape("turtle")

alex.color("red")

alex.left(160)
alex.forward(100)
alex.right(43)
alex.forward(100)
alex.left(270)
alex.forward(100)
alex.right(97)
alex.forward(100)
alex.right(43)
alex.forward(100)
alex.left(200)
alex.forward(100)
alex.right(940)
alex.forward(100)
alex.left(17)
alex.forward(100)
alex.right(86)
alex.forward(100)

    

"""using turtle.mainloop instead of wn.mainloop since it gives error "_Screen' object has
no attribute 'mainloop' """
turtle.mainloop()     # Wait for user to close window