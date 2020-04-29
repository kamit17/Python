#Write a program to draw a face of a clock

import turtle
t = turtle.Turtle()
wn = turtle.Screen()
#t= turtle.Turtle()
t.shape('turtle')
for _ in range(12):
    t.penup()
    t.forward(80)
    t.pendown()
    t.forward(10)
    t.penup()
    t.forward(30)
    t.stamp()
    t.forward(-120)
    t.right(30)
t.stamp()
wn.mainloop()

