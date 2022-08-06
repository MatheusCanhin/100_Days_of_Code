from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """Responsável pela criação de placar e mensagens na tela"""

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-270, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Atualiza o scoreboard"""
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)


    def increase_level(self):
        """Aumenta o level, aumentando a velocidade dos carros"""
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        """Mostra game over na tela"""
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
