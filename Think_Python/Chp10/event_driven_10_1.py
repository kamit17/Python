import turtle

turtle.setup(400,500)             #Determine the window size
wn = turtle.Screen()              # Get a reference to the window
wn.title('Handling Keypresses!')  #Change the window title
wn.bgcolor("lightgreen")          #Set the background color
tess = turtle.Turtle()            #Create the turtle

#The next four functions are our "event handlers".
def h1():
    tess.forward(30)

def h2():
    tess.left(45)

def h3():
    tess.right(45)
def h4():
    wn.bye()                         #Close down the turtle window

#These lines wireup keypresses to the handlers we have defined.
wn.onkey(h1,"Up")
wn.onkey(h2,'Left')
wn.onkey(h3,'Right')
wn.onkey(h4,'q')

#Now we need to tell the window to start listening for events,
#If any of the keys we are monitoring is pressed, its handler
#will be called
wn.listen()
wn.mainloop()

