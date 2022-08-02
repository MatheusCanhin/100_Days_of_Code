from turtle import Screen
from time import sleep
from snake import Snake

# Criando a tela, formatando seu tamanho, cor do fundo, titulo e cancelando o tracer
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Criando o objeto snake, criando um listener e fazer com que o sentido da snake mude conforme a tecla
snake = Snake()
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")


# Criando o loop para realizar a movimentação da Snake
game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.1)

    snake.move()

screen.exitonclick()
