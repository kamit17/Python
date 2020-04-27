# Extend your program above. Draw five stars, but between each, pick up the pen, move forward by 350 units, turn right by 144, put the pen down, and draw the next star. You’ll get something like this:


import turtle as t
def star(side):
    t.pendown()  
    
    for i in range(5):  #Draws pentagram
        t.forward(side)
        t.right(144)
    t.penup()
    
     #t.penup()   

wn = t.Screen()
wn.bgcolor("Hot Pink")

t= t.Turtle()
t.penup()
t.hideturtle()

t.backward(175)          # Position t at a convenient spot.
t.left(90)
t.forward(60)
t.right(90)

for a in range(5):
    star(100)
    t.forward(350)
    t.right(144)
#star(100)
wn.mainloop()
