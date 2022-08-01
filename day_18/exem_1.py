# Objetivo desse código é fazer com que o Turtle desenhe figuras do triângulo até o decagono
from turtle import Turtle
from random import choice

tim = Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(sides):
    angle = 360/sides
    for i in range(sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3, 10):
    tim.color(choice(colours))
    draw_shape(shape_side_n)

