from turtle import Turtle

# Constantes
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """Criando a classe Snake para o jogo"""

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Cria a cobra inicial, utilizando as posições iniciais"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Adiciona um segmento a cobra"""
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """Adiciona um segmento ao final da cobra"""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Realiza o movimento da cobra, basicamente faz com que a última posição assuma o lugar da próxima"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Verifica se a cobra esta indo para baixo, se estiver não faz nada.
        Se não estiver muda o sentido para cima"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Verifica se a cobra esta indo para cima, se estiver não faz nada.
        Se não estiver muda o sentido para baixo"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Verifica se a cobra esta indo para direita, se estiver não faz nada.
        Se não estiver muda o sentido para esquerda"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Verifica se a cobra esta indo para esquerda, se estiver não faz nada.
        Se não estiver muda o sentido para direita"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)




