# Objetivo é fazer com que desenhemos caminhos aleatórios com cores aleatórias, devemos utilizar o pensize para mexer com
# a espessura, speed para a velocidade e o setheading.
import random
from turtle import Turtle, colormode
from random import choice, randint

tim = Turtle()
colormode(255)

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b

print(random_color())
directions = [0, 90, 180, 270]

for _ in range(200):
    tim.color(random_color())
    tim.pensize(5)
    tim.speed('fastest')
    tim.forward(30)
    tim.setheading(choice(directions))
