from turtle import Screen, Turtle
from paddle import SidePaddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(600, 600)
screen.title("Pong")
screen.tracer(0)

tim = Turtle()
tim.pencolor("white")
tim.penup()
tim.goto(0, 500)
tim.right(90)
for i in range(100):
    tim.forward(10)
    tim.pendown()
    tim.forward(10)
    tim.penup()


l_paddle = SidePaddle((-290, 0))
r_paddle = SidePaddle((280, 0))
ball = Ball()
scoreboard = Scoreboard()
scoreboard.update_score()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() < -275 or ball.ycor() > 275:
        ball.bounce()

    # Right paddle
    if ball.xcor() > 250:
        if r_paddle.ycor() + 50 > ball.ycor() > r_paddle.ycor() - 50:
            ball.hit()
    if ball.xcor() > 300:
        ball.new_game()
        scoreboard.l_point()
        scoreboard.update_score()

    # Left paddle
    if ball.xcor() < -260:
        if l_paddle.ycor() + 50 > ball.ycor() > l_paddle.ycor() - 50:
            ball.hit()
    if ball.xcor() < -310:
        ball.new_game()
        scoreboard.r_point()
        scoreboard.update_score()

    if scoreboard.r_score == 11:
        scoreboard.r_win()
        game_is_on = False

    if scoreboard.l_score == 11:
        scoreboard.l_win()
        game_is_on = False


screen.exitonclick()
