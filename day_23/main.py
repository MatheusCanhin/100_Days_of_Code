import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Criando a tela
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Criando objetos
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Criando o listener para movimentar a tartaruga
screen.listen()
screen.onkey(player.go_up, "Up")

# Criando o loop
game_is_on = True
while game_is_on:
    time.sleep(0.08)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detectando a colisão do carro com a tartaruga
    for car in car_manager.all_cars:
        if car.distance(player) < 18:
            game_is_on = False
            scoreboard.game_over()

    # Detectando se a tartaruga atingiu o objetivo
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()



screen.exitonclick()