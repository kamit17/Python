import turtle
window = turtle.Screen()
pirate = turtle.Turtle() 
for turn in [160, -43, 270, -97, -43, 200, -940, 17, -86]:
    pirate.left(turn)
    pirate.forward(100)
    print (pirate.position())