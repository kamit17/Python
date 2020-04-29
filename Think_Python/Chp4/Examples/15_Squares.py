import turtle

def draw_multicolor_square(animal,size):
    """Make animal draw a multi-color square of given size"""
    for color in ["red","purple","hotpink","blue"]:
        animal.color(color)
        animal.forward(size)
        animal.left(90)
        

window = turtle.Screen() # Set up the window and its attributes
window.bgcolor("lightgreen")

tess = turtle.Turtle() # create tess and set some attributes
tess.pensize(5)


size = 20 # Size of the smallest square
#draw_multicolor_square(tess,size)
for _ in range(22):
    draw_multicolor_square(tess,size)
    size += 10 #Increase the size the next time around
    tess.forward(10)  # Moves tess along a bit
    tess.right(18)      # and give her some turn
    

window.mainloop()