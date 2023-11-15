from turtle import Screen, Turtle
from paddle import SidePaddle, DeckPaddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(600, 600)
screen.title("Pong")
screen.tracer(0)

# Dashed line
tim = Turtle()
tim.pencolor("white")
tim.penup()
tim.goto(-320, 320)
tim.right(45)
for i in range(100):
    tim.forward(10)
    tim.pendown()
    tim.forward(10)
    tim.penup()
tim.goto(324, 333)
tim.right(90)
for i in range(100):
    tim.forward(10)
    tim.pendown()
    tim.forward(10)
    tim.penup()

l_paddle = SidePaddle((-295, 0))
r_paddle = SidePaddle((285, 0))
u_paddle = DeckPaddle((0, 295))
d_paddle = DeckPaddle((0, -290))
ball = Ball()
scoreboard = Scoreboard()
scoreboard.update_score()

screen.listen()
# Right paddle
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
# Left paddle
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
# Upper paddle
screen.onkey(u_paddle.go_left, "z")
screen.onkey(u_paddle.go_right, "u")
# Down paddle
screen.onkey(d_paddle.go_left, "v")
screen.onkey(d_paddle.go_right, "b")

game_is_on = True
r_in_game = True
l_in_game = True
u_in_game = True
d_in_game = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Right paddle
    if r_in_game:
        if ball.xcor() > 280:
            if r_paddle.ycor() + 50 > ball.ycor() > r_paddle.ycor() - 50:
                if r_paddle.ycor() < ball.ycor():
                    ball.hit_up()
                if r_paddle.ycor() > ball.ycor():
                    ball.hit_down()
                else:
                    ball.hit()
        if ball.xcor() > 300:
            ball.new_game()
            scoreboard.r_point()
            scoreboard.update_score()
        if scoreboard.r_score == 8:
            r_paddle.color("black")
            r_in_game = False
        if not l_in_game and not u_in_game and not d_in_game:
            scoreboard.r_win()
            game_is_on = False
    else:
        if ball.xcor() > 280:
            ball.hit()

    # Left paddle
    if l_in_game:
        if ball.xcor() < -280:
            if l_paddle.ycor() + 50 > ball.ycor() > l_paddle.ycor() - 50:
                if l_paddle.ycor() < ball.ycor():
                    ball.hit_up()
                if l_paddle.ycor() > ball.ycor():
                    ball.hit_down()
                else:
                    ball.hit()
        if ball.xcor() < -300:
            ball.new_game()
            scoreboard.l_point()
            scoreboard.update_score()
        if scoreboard.l_score == 8:
            l_paddle.color("black")
            l_in_game = False
        if not r_in_game and not u_in_game and not d_in_game:
            scoreboard.l_win()
            game_is_on = False
    else:
        if ball.xcor() < -280:
            ball.hit()

    # Upper paddle
    if u_in_game:
        if ball.ycor() > 280:
            if u_paddle.xcor() + 50 > ball.xcor() > u_paddle.xcor() - 50:
                if u_paddle.xcor() < ball.xcor():
                    ball.bounce_right()
                if u_paddle.xcor() > ball.xcor():
                    ball.bounce_left()
                else:
                    ball.bounce()
        if not l_in_game and not r_in_game and not d_in_game:
            game_is_on = False
    else:
        if ball.ycor() > 280:
            ball.bounce()

    # Down paddle
    if d_in_game:
        if ball.ycor() < -275:
            if d_paddle.xcor() + 50 > ball.xcor() > d_paddle.xcor() - 50:
                if d_paddle.xcor() < ball.xcor():
                    ball.bounce_right()
                if d_paddle.xcor() > ball.xcor():
                    ball.bounce_left()
                else:
                    ball.bounce()
    else:
        if ball.ycor() < -275:
            ball.bounce()

screen.exitonclick()
