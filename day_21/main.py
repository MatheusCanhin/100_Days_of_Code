from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Criando a tela, formatando seu tamanho, cor do fundo, titulo e cancelando o tracer
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Criando o objeto snake, criando um listener e fazer com que o sentido da snake mude conforme a tecla
snake = Snake()
food = Food()
scoreboard = Scoreboard()


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

    # Detectando a colisão com a comida (distance metod)
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increse_score()

    # Detectando colisão com a parede
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.xcor() < -280:
        scoreboard.game_over()
        game_is_on = False

    # Detectando colisão com a calda
    for segment in snake.segments[1:]:
        # if head collides with any segment in the tail:
        # trigger game_over
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()



screen.exitonclick()
