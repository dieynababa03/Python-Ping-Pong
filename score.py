from turtle import Turtle
class Score():
  def __init__(self, position):
    self.score = Turtle()
    self.score.penup()
    self.score.hideturtle()
    self.score.setposition(position)
    self.scoreVal = 0
    self.score.color("#5F9EA0")
  def setScore(self):
    self.score.write(f"{self.scoreVal}", font=('Tsukushi A Round Gothic', 40, 'normal'))
  def updateScore(self):
    self.scoreVal +=1
    self.score.clear()
