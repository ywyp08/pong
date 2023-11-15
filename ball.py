from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.2

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= (-1)
        self.move_speed = self.move_speed / 1

    def bounce_left(self):
        self.y_move *= (-1)
        self.x_move -= 5
        self.move_speed = self.move_speed / 1

    def bounce_right(self):
        self.y_move *= (-1)
        self.x_move += 5
        self.move_speed = self.move_speed / 1

    def hit(self):
        self.x_move *= (-1)
        self.move_speed = self.move_speed / 1.5

    def hit_up(self):
        self.x_move *= (-1)
        self.y_move += 5
        self.move_speed = self.move_speed / 1

    def hit_down(self):
        self.x_move *= (-1)
        self.y_move -= 5
        self.move_speed = self.move_speed / 1

    def new_game(self):
        self.move_speed = 0.2
        self.goto(0, 0)
        self.hit()

