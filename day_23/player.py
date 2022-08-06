from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """responsável pela criação do player e suas ações"""

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.go_to_start()

    def go_up(self):
        """Faz com que a tartaruga se mova para cima"""
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        """Faz com que o player volte para o inicio da tela"""
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        """Verifica se o jogador chegou ao final"""
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
