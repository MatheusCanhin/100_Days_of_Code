from turtle import Turtle
ALIGMENT = "center"
FONT = ("Arial", 24, "normal")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.goto(0, 265)
        self.update_scoreboard()

    def update_scoreboard(self):
        "Escreve o placar na tela"
        self.clear()
        self.write(f"score: {self.score} High Score: {self.high_score}", align=ALIGMENT, font=FONT)

    def increse_score(self):
        """Aumenta um valor no placar"""
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0



