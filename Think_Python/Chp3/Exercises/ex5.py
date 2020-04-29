# Use for loops to make a turtle draw these regular polygons(regular means all sides the same
# #  lengths,all angles the same):
# • An equilateral triangle
# • A square
# • A hexagon (six sides)
# • An octagon (eight sides)



import turtle   #Allows us to use turtles
wn = turtle.Screen() # creates a playground for turtles
tess = turtle.Turtle() # Create a turtle, assign to tess
for _ in range(3):

    tess.left(120) # Move tess along
    tess.forward(90)
    
tess.color("blue")    
tess.forward (20)

# • A square
for _ in range(4):
  tess.forward(40)
  tess.left(90) # Move tess along
  
tess.right(120)
tess.color("red")

# • A hexagon
for _ in range(6):
    tess.forward(90)
    tess.left(60) # Move tess along
  
tess.forward(80)
tess.color("yellow")

# • An octagon (eight sides)
for _ in range(8):
 # Move tess along
  tess.forward(90)
  tess.right(45)
  
window.mainloop()