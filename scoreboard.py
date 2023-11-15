from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0

    def update_score(self):
        self.clear()
        self.goto(-100, -40)
        self.write(self.l_score, align="center", font=("Courier", 60, "normal"))
        self.goto(100, -40)
        self.write(self.r_score, align="center", font=("Courier", 60, "normal"))
        self.goto(0, -120)

    def l_point(self):
        self.l_score += 1

    def r_point(self):
        self.r_score += 1

    def l_win(self):
        self.goto(0, -40)
        self.write('W', align="center", font=("Courier", 60, "normal"))

    def r_win(self):
        self.goto(0, -40)
        self.write('W', align="center", font=("Courier", 60, "normal"))
