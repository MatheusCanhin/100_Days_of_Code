#Como desafio temos que criar um algoritmo que resolva todos os casos da seguinte fase 
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json



# Todas as funções não definidas no código são funções criadas no site do jogo.
def turn_right():
    turn_left()
    turn_left()
    turn_left()

#Evita que o robo entre em loop no começo
while front_is_clear():
    move()
turn_right()

#Reaiza as checagens até chegar no objetivo
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else: 
        turn_left()