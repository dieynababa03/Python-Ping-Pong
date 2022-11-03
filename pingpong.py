from turtle import Turtle, Screen
from player import Player
from board import Board
from score import Score
from ball import Ball
import time

screen = Screen()
screen.bgcolor('#DCDCDC')
screen.screensize(600, 600)
screen.tracer(0)

#Creating both players
player1 = Player((-320, 0))
player1.createPlayer()


player2 = Player((320, 0))
player2.createPlayer()

#Drawing the center line
boardCenter = Board()
boardCenter.drawCenter()

#Creating the score board for both players
scoreP1 = Score((-70, 270))
scoreP1.setScore()

scoreP2 = Score((60, 270))
scoreP2.setScore()

#Creating my ping pong ball object
ball = Ball()


screen.listen()
#Setting player 1's movement keys
screen.onkey(key="Up", fun=player1.moveUp)
screen.onkey(key="Down", fun=player1.moveDown)

#Setting player 2's movement keys
screen.onkey(key="w", fun=player2.moveUp)
screen.onkey(key="s", fun=player2.moveDown)

game_on = True
while game_on:
  time.sleep(0.1)
  screen.update()
  ball.ballMove()

  if ball.ball.ycor() > 290 or ball.ball.ycor() < -290:
      ball.ballBounce()

  if ball.ball.distance(player2.player) < 40 and ball.ball.xcor() > 290:
    ball.paddleBounce()
  if ball.ball.distance(player1.player) < 40 and ball.ball.xcor() > -315:
    ball.paddleBounce()

  if ball.ball.xcor() > 325:
    ball.resetBall()
    scoreP1.updateScore()
    scoreP1.setScore()
  if ball.ball.xcor() < -325:
    ball.resetBall()
    scoreP2.updateScore()
    scoreP2.setScore()
    


screen.exitonclick()