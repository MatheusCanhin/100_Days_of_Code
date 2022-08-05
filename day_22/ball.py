from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 5
        self.y_move = 5
        self.move_speed = 0.05


    def move(self):
        """Realiza o movimento da bola"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Inverte o sentido do movimento no sentido Y e aumenta a velocidade da bolinha"""
        self.y_move *= -1
        self.move_speed *= 0.9

    def bounce_x(self):
        """Inverte o sentido do movimento no sentido X e aumenta a velocidade da bolinha"""
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.05
        self.bounce_x()
