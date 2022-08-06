from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    """Responsável pela criação dos carros e seus movimentos"""

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        """Cria um novo carro"""
        random_chance = randint(1, 6)# foi utilizado para diminuir a frequência da criação dos carros
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=0.6, stretch_len=1.4)
            new_car.penup()
            new_car.color(choice(COLORS))
            random_y = randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        """Movimenta os carros"""
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        """Aumenta a velocidade do carro"""
        self.car_speed += MOVE_INCREMENT
