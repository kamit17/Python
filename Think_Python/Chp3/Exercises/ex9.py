"Write a program to draw a star"
import turtle as t
wn = t.Screen()
t= t.Turtle()
t.hideturtle()
for i in range(5):
    t.forward(150)
    t.right(144)  # 2 complete rotations(720) // 5 = 144
wn.mainloop()
