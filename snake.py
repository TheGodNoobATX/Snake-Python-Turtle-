from turtle import *
import random
import time

def generate_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"

def playing_area():
    pen = Turtle()
    pen.ht()
    pen.speed(0)
    pen.color("#004400")
    pen.begin_fill()
    pen.goto(-240,240)
    pen.goto(240,240)
    pen.goto(240,-240)
    pen.goto(-240,-240)
    pen.goto(-240,240)
    pen.end_fill()
    
class Head(Turtle):
  def __init__(self, screen, body):
    super().__init__()
    self.screen = screen
    self.body = body
    self.ht()
    self.speed(0)
    self.color("#00FF00")
    self.shape("square")
    self.penup()
    self.setheading(0)
    self.showturtle()

  def up(self):
    if self.heading() != 270:
      self.setheading(90)
      turningPoints.append([self.pos(),90])

  def down(self):
    if self.heading() != 90:
      self.setheading(270)
      turningPoints.append([self.pos(),270])


  def left(self):
    if self.heading() != 0:
      self.setheading(180)
      turningPoints.append([self.pos(),180])


  def right(self):
    if self.heading() != 180:
      self.setheading(0)
      turningPoints.append([self.pos(),0])


class Segment(Turtle):
  def __init__(self, head):
    super().__init__()
    self.head = head
    self.ht()
    self.speed(0)
    self.color("#00FF00")
    self.shape("square")
    self.penup()
    self.setheading(head.heading())
    self.showturtle()
    if head.heading() == 0:
      self.goto(head.pos() - [15*(len(head.body)+1),0])
    elif head.heading() == 90:
      self.goto(head.pos() - [0,15*(len(head.body)+1)])
    elif head.heading() == 180:
      self.goto(head.pos() - [-15*(len(head.body)+1),0])
    if head.heading() == 270:
      self.goto(head.pos() - [0,-15*(len(head.body)+1)])

  def move(self, other):
    pass

class Apple(Turtle):
  def __init__(self):
    super().__init__()
    self.ht()
    self.speed(0)
    self.shape("circle")
    self.penup()
    self.color("#FF0000")
    self.goto(150,0)
    self.showturtle()

  def relocate(self):
    self.goto(random.randint(-200,200),random.randint(-200,200))

screen = Screen()
screen.bgcolor("black")
screen.setup(700,700)
playing_area()
body = []
turningPoints = []
alive = True
head = Head(screen,body)
apple = Apple()
onkeypress(head.up,'Up')
onkeypress(head.down,'Down')
onkeypress(head.left,'Left')
onkeypress(head.right,'Right')
# Key Binding. Connects key presses and mouse clicks with function calls
screen.listen()

while alive == True:
  head.forward(1)
  for i in range(len(body)):
    body[i].forward(1)
    for i2 in range(len(turningPoints)):
      if body[i].pos() == turningPoints[i2][0]:
        body[i].setheading(turningPoints[i2][1])
  if head.xcor() <= -240 or head.xcor() >= 240 or head.ycor() <= -240 or head.ycor() >= 240:
    alive = False
  if head.xcor() <= apple.xcor() + 10 and head.xcor() >= apple.xcor() - 10 and head.ycor() <= apple.ycor() + 10 and head.ycor() >= apple.ycor() - 10:
    apple.relocate()
    body.append(Segment(head))
  for part in body:
    if head.xcor() <= part.xcor() + 7 and head.xcor() >= part.xcor() - 7 and head.ycor() <= part.ycor() + 7 and head.ycor() >= part.ycor() - 7:
      alive = False
for i in range(len(body)):
  body[i].ht()
  time.sleep(0.5)
head.ht()

screen.exitonclick()