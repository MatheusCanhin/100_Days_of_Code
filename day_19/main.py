from turtle import Screen, Turtle
from random import randint

is_race_on = False
colors = ['red', 'blue', 'orange', 'yellow', 'purple', 'green']
y_position = [-125, -75, -25, 25, 75, 125]
all_turtles = []

# Criando a tela e seu tamanho
screen = Screen()
screen.setup(width=500, height=400)

# Criando o input da tela
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)

if user_bet:
    is_race_on = True
else:
    print("select one of rainbow colors")
    exit()

# Criando todas as tartaugas e colocando elas em seus lugares
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-200, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

# Enquanto nenhuma tartaruga ganhou, executa o loop
while is_race_on:

    for turtle in all_turtles:

        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")

        rand_distance = randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
