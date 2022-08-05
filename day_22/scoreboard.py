from turtle import Turtle

ALIGMENT = "center"
FONT = ("Arial", 60, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 210)
        self.write(self.l_score, align=ALIGMENT, font=FONT)
        self.goto(100, 210)
        self.write(self.r_score, align=ALIGMENT, font=FONT)
        self.make_line()


    def r_point(self):
        self.r_score += 1

    def l_point(self):
        self.l_score += 1


    def make_line(self):
        self.goto(0, -300)
        for i in range(0, 30):
            self.setheading(90)
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)



