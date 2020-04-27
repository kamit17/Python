# Write a void function to draw a star, where the length of each
# side is 100 units. (Hint: You should turn the turtle by 144 degrees
# at each point.)

import turtle as t
def star(side):
    
    for i in range(5):
        t.forward(side)
        t.right(144)
    
        

wn = t.Screen()
t= t.Turtle()
t.hideturtle()
# for i in range(5):
#     t.forward(150)
#     t.right(144)  # 2 complete rotations(720) // 5 = 144

star(100)
wn.mainloop()

