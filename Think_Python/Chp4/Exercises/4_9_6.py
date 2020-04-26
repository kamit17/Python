import turtle




def draw_poly(t, n, z):
    for i in range(0, n):
        t.forward(z)
        t.left(360 / n)


def draw_equitriangle(t, sz):
    draw_poly(t, 3, sz)
    
window = turtle.Screen()            # Set up a window and some attributes
window.bgcolor("lightgreen")

Tom = turtle.Turtle()
Tom.color("HotPink")
Tom.pensize(3)

draw_poly(Tom,8,50)
draw_equitriangle(Tom, 100)
Window.mainloop()