#Make a simulated pirate and a place for him to suble around
import turtle
wn = turtle.Screen()
pirate = turtle.Turtle()


#raw data about how he stumbles
turns_and_steps= [(160,20),(-43,10),(270,8),(-43,12)]

#Simulate the actual stumbling around

for x in turns_and_steps:
    #The Pirate turns
    pirate.left(x[0])
    #He takes some steps forward
    pirate.forward(10 * x[1])

#Keep the screen open till the user closes it.
wn.mainloop()
