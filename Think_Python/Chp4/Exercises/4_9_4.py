# Draw this pretty pattern
import turtle

def draw_poly(t,n,side):
    """
        Makes a ploygon of n sides with each side of lenght side .
    """
    angle = 360 / n
    for _ in range (n):
        t.forward(side)
        t.right(angle)

window  = turtle.Screen()   # setup window and attributes
window.bgcolor("lightgreen")
window.title("Pretty Pattern")


alex = turtle.Turtle()  # setup turtle and attributes
alex.color("blue")
alex.pensize(3)

for i in range(0,20):
    draw_poly(alex,4,100)
    alex.right(18)  # the angle 18 360/n
    
window.mainloop()

