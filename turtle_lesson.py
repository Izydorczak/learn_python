
import turtle

wn = turtle.Screen()
diane = turtle.Turtle()
diane.forward(130)
diane.left(90)
diane.forward(60)
wn.exitonclick()


import turtle

wn = turtle.Screen()
diane = turtle.Turtle()
diane.forward(100)
diane.left(72)
diane.forward(100)
diane.left(72)
diane.forward(100)
diane.left(72)
diane.forward(100)
diane.left(72)
diane.forward(100)
diane.left(72)
wn.exitonclick()


for sideNum in [1,2,3,4,5]:
  diane.forward(100)
  diane.left(72)
  
  
for sideNum in range(5):
  diane.forward(100)
  diane.left(72)
  
  
diane.shape("turtle")
diane.shape("square")
diane.penup()          #follow this with one of the movement commands
diane.pendown()
diane.circle(6)
diane.pensize(4)



for aColor in ["red", "blue", "yellow", "green", "purple"]:
  diane.color(aColor)
  diane.forward(100)
  diane.left(72)
  
  
  
def drawSquare():
  diane.penup()
  diane.goto(50,50)
  diane.pendown()
  for side in range(4):
      diane.forward(50)
      diane.right(90)
      
      
drawSquare()


def drawSquare(x,y):
  diane.penup()
  diane.goto(x,y)
  diane.pendown()
  for side in range(4):
      diane.forward(50)
      diane.right(90)
      
drawSquare(50,50)
drawSquare(100,200)
