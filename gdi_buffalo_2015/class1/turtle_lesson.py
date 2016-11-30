
import turtle

wn = turtle.Screen()
alex = turtle.Turtle()
alex.forward(150)
alex.left(90)
alex.forward(75)
wn.exitonclick()


import turtle

wn = turtle.Screen()
alex = turtle.Turtle()
alex.forward(100)
alex.left(72)
alex.forward(100)
alex.left(72)
alex.forward(100)
alex.left(72)
alex.forward(100)
alex.left(72)
alex.forward(100)
alex.left(72)
wn.exitonclick()


for sideNum in [1,2,3,4,5]:
  alex.forward(100)
  alex.left(72)
  
  
for sideNum in range(5):
  alex.forward(100)
  alex.left(72)
  
  
alex.shape("turtle")
alex.shape("square")
alex.penup()
alex.pendown()
alex.circle(6)
alex.pensize(4)



for aColor in ["red", "blue", "yellow", "green", "purple"]:
  alex.color(aColor)
  alex.forward(100)
  alex.left(72)
  
  
  
def drawSquare():
  alex.penup()
  alex.goto(50,50)
  alex.pendown()
  for side in range(4):
      alex.forward(50)
      alex.right(90)
      
      
drawSquare()


def drawSquare(x,y):
  alex.penup()
  alex.goto(x,y)
  alex.pendown()
  for side in range(4):
      alex.forward(50)
      alex.right(90)
      
drawSquare(50,50)
drawSquare(100,200)
