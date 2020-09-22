import turtle
turtle.setup(400,500)        #Determine the window size
wn = turtle.Screen()         #Get a reference to the window
wn.bgcolor("lightgreen")
wn.title("Handling mouse clicks!")
tess = turtle.Turtle()        #Crate two turtles
tess.color("orange")
alex = turtle.Turtle()
alex.color("blue")
alex.forward(100)

def handler_for_tess(x,y):
    wn.title('Tess clicket at {0},{1}'.format(x,y))
    tess.left(42)
    #tess.right(84)
    tess.forward(30)

def handler_for_alex(x,y):
    wn.title("Alex clicket at {0},{1}".format(x,y))
    alex.left(84)
    alex.forward(50)

tess.onclick(handler_for_tess)
alex.onclick(handler_for_alex)

wn.mainloop()
