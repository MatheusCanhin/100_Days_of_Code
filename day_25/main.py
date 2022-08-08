from turtle import Screen, Turtle, shape
import pandas as pd

# Criando a tela e fazendo a imagem do Brasil ser utilizada
image = "brasil_states.gif"
screen = Screen()
screen.title("BR States Game")
screen.addshape(image)
shape(image)

# função utilizada para pegar as coordenadas no mapra
# def get_mouse_click(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click)

# lendo o arquivo csv, criando uma lista com os estados e criando uma lista vazia
data = pd.read_csv("states.csv")
states = data.state.to_list()
guessed_states = []


while len(guessed_states) < 27:

    #Recebendo a entrada do usuário e tratando a mesma
    answer_state = screen.textinput(title=f"{len(guessed_states)}/27 Estados do Brasil",
                                    prompt="Digite a sigla do estado:").upper().strip()

    # verifica se a entrada do usuário é a palavra sair, para sair do jogo
    if answer_state == "SAIR":
        missing_states = []
        for state in states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv") # cria um novo arquivo csv com as respostas que o usuário não colocou
        break

    # Verifica se a resposta do usuário está dentro dos estados, caso sim, remove o estado da lista e escreve na tela
    if answer_state in states:
        states.remove(answer_state)
        guessed_states.append(answer_state)
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_date = data[data.state == answer_state]
        t.goto(int(state_date.x), int(state_date.y))
        t.write(answer_state)

