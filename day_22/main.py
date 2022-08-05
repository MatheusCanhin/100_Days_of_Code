from turtle import Turtle, Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
from time import sleep


# Criando a tela
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)



# Criando a raquete da direita
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-360, 0))
ball = Ball()
scoreboard = Scoreboard()

# Criando o listener
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# Atualizando a tela
game_is_on = True
while game_is_on:
    screen.update()
    sleep(ball.move_speed) #utilizado o 'time' para fazer com que o programa de um tempo para realizar o movimento da bola
    ball.move()

    # Detectando a colisão com a parede
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detectando a colisão com a raquete da direita:
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -335:
        ball.bounce_x()

    # Detectando se a raquete direita errou
    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.l_point()
        scoreboard.update_scoreboard()

    # Detectando se a raquete esquerda errou
    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.r_point()
        scoreboard.update_scoreboard()






screen.exitonclick()
