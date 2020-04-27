#Football Formation Challenge - www.101computing.net/football-formation/
import pitch
import turtle

#A Procedure to draw a player at the given position
def drawPlayer(color,x,y,label):
  screen = turtle.Screen()
  screen.tracer(0)
  myPen = turtle.Turtle()
  myPen.hideturtle()
  myPen.penup()
  myPen.goto(x,y)
  myPen.fillcolor(color)
  myPen.begin_fill()
  myPen.circle(10)
  myPen.end_fill()
  screen.tracer(1)  
  myPen.penup()
  myPen.goto(x+10,y)
  myPen.color(color)
  myPen.write(label)

#MAIN PROGRAM STARTS HERE
pitch.drawPitch()

drawPlayer("blue",-0,-194,"Goal Keeper") 
drawPlayer("yellow",-50,-120,"Centre Back") 
drawPlayer("yellow",50,-120,"Centre Back") 
#Add more players using the relevant parameters

