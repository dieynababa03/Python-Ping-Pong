from turtle import Turtle
class Player():
  def __init__(self, position):
    self.player = Turtle()
    self.player.penup()
    self.player.setposition(position)
  def createPlayer(self):
    self.player.penup()
    self.player.shape("square")
    self.player.color("#5F9EA0")
    self.player.shapesize(4, 0.7)
  def moveUp(self):
    self.player.goto(self.player.xcor(), self.player.ycor() + 25)

  def moveDown(self):
    self.player.goto(self.player.xcor(), self.player.ycor() - 25)

  