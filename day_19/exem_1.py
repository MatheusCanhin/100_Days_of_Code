# Como primeiro desafio devemos criar uma tela, com a seta no centro e ao pressionar a tecla "w" a seta
# deve ir para frente, "s" para trás, "a" para girar no sentido horário, "d" no sentido antiorário e "c" para limpar td

from turtle import Screen, Turtle

tim = Turtle()
tim.speed(0)

def move_forward():
    """Faz o cursor andar para frente"""
    tim.forward(10)

def move_backward():
    """Faz o cursor andar para trás"""
    tim.backward(10)

def rotate_r():
    """Faz o cursor virar para a direita em 10 graus"""
    tim.right(10)

def rotate_l():
    """Faz o cursor virar para a esquerda em 10 graus"""
    tim.left(10)

def clear():
    """limpa a tela e faz com que o cursor volte para o ponto de inicio"""
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen = Screen()

# Cria o listener e verificam a ação de algumas teclas
screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='a', fun=rotate_r)
screen.onkey(key='d', fun=rotate_l)
screen.onkey(key='c', fun=clear)

# Sai da tela ao clicar em qualquer lugar
screen.exitonclick()