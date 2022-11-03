from turtle import Turtle
class Board:
  def __init__(self):
    self.centerLine = Turtle()
    self.centerLine.color("#5F9EA0")
    self.centerLine.setpos(0, 350)
    self.centerLine.setheading(270)
    self.centerLine.width(3)
    self.centerLine.shape("square")
  def drawCenter(self):
    for i in range(0, 75):
      self.centerLine.forward(11)
