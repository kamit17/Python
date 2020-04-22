import turtle

def draw_rectangle(animal,width,height):
    """Get animal to draw a rectange of given width and height"""
    for _ in range(2):
        animal.forward(width)
        animal.left(90)
        animal.forward(height)
        animal.left(90)
def draw_square(animal,size):
    draw_rectangle(animal,size,size)

window = turtle.Screen() # setup the window and its attributes
window.bgcolor("lightgreen")
window.title('Alex meets a function')

alex = turtle.Turtle() # create alex
tess = turtle.Turtle() # create tess
#draw_rectangle(alex,50,25) # call the function to draw the square
draw_square(tess,50)
window.mainloop()