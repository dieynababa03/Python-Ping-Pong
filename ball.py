from turtle import Turtle
import random
class Ball:
  def __init__(self):
    self.ball = Turtle()
    self.ball.penup()
    self.ball.shape("circle")
    self.ball.color("#5F9EA0")
    self.ball.shapesize(1.5, 1.5)
    self.x_move = 10
    self.y_move = 10
  def ballMove(self):
    self.ball.goto(self.ball.xcor() + self.x_move, self.ball.ycor() + self.y_move)
  def ballBounce(self):
    self.y_move *= -1
  def paddleBounce(self):
    self.x_move *= -1
  def resetBall(self):
    self.ball.setposition(0.00, 0.00)

