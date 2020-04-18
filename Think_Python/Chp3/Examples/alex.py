import turtle   #Allows us to use turtles
wn = turtle.Screen() # creates a playground for turtles
alex = turtle.Turtle() # Create a turtle, assign to alex
#alex.left(3645)
print("the type of alex is ",type(alex))
alex.color("red")

alex.forward(50)  # Tell alex to move forward by 50 units
alex.left(90)     # Tell alex to turn by 90 degrees
alex.forward(30)  # Complete the second side of a rectangle

"""using turtle.mainloop instead of wn.mainloop since it gives error "_Screen' object has
no attribute 'mainloop' """
turtle.mainloop()     # Wait for user to close window
