import turtle

def draw_square(animal,size):
    for _ in range(4):
        animal.forward(size)
        animal.left(90)
        
window = turtle.Screen()  # setup window and its attribuets

tess = turtle.Turtle()

draw_square(tess,50)

window.mainloop()
