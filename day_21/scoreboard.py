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
        self.goto(0, 265)
        self.update_scoreboar()

    def update_scoreboar(self):
        "Escreve o placar na tela"
        self.write(f"score: {self.score}", align=ALIGMENT, font=FONT)

    def increse_score(self):
        """Aumenta um valor no placar"""
        self.score += 1
        self.clear()
        self.update_scoreboar()

    def game_over(self):
        """Finaliza o jogo"""
        self.goto(0, 0)
        self.write("Game Over", align=ALIGMENT, font=FONT)


