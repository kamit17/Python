import turtle

def make_window(color,title):
    """
        Setup the window with the given background color and title.
        Returns the new Window.
    """
    window = turtle.Screen()  #stup window and its attributes
    window.bgcolor(color)
    window.title(title)
    return window

def make_turtle(color,size):
    """
        Setup a turtle with the given color and pen size.
        Returns the new turtle.
    """
    animal = turtle.Turtle()
    animal.color(color)
    animal.pensize(size)
    #animal.speed(-20)
    return animal

wn = make_window("lightgreen","Tess and Alex dancing")
tess = make_turtle("hotpink",5)
alex = make_turtle("black",1)
dave = make_turtle("yellow",2)