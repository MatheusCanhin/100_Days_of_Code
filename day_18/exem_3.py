# Devemos desenhar um spirograph, para isso precisamos saber como desenhar um círculo e como mudar a direção do turtle
from turtle import Turtle, colormode, Screen
from random import randint

tim = Turtle()
tim.speed('fastest')
colormode(255)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


def draw_spirograoh(size_of_gap):
    for i in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograoh(10)

screen = Screen()
screen.exitonclick()
