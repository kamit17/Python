# Write a void function draw_poly(t, n, sz) which makes a turtle draw a regular polygon. When called with draw_poly(tess, 8, 50),itwilldrawashapelikethis:

import turtle

def draw_poly(t,n,sz):
    angle = 360 / n
    for _ in range (n):
        t.forward(sz)
        t.right(angle)
        

window = turtle.Screen()            # Set up a window and some attributes
window.bgcolor("lightgreen")

alex = turtle.Turtle()              # Set up a turtle and some attributes
alex.color("HotPink")
alex.pensize(3)

draw_poly(alex,8,50)
window.mainloop()