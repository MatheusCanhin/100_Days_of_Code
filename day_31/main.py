from tkinter import *
import pandas as pd
from random import choice
from tkinter import messagebox
import pandas.errors

# Constantes
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}


try:
    try:
        data = pd.read_csv("data/words_to_learn.csv")  # lê o csv
        if len(data) > 0:  # Verifica se existem palavras a serem aprendindas
            pass
        else:
            messagebox.showinfo(title="Congratulations!!!!", message="You learned all the words!!!")  # exibe mensagem
            exit()
    except pandas.errors.EmptyDataError:
        messagebox.showinfo(title="Congratulations!!!!", message="Your data is already empty")  # exibe mensagem
        exit()
except FileNotFoundError:
    original_data = pd.read_csv("data/english_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    """Tem a função de ir para a próxima carta e Verificar se existem palavras para serem aprendidas"""

    if len(to_learn) > 0:
        global current_card, flip_timer  # Utilizando algumas váriaveis globais
        screen.after_cancel(flip_timer)  # Faz com que o primeiro timer criado, seja cancelado
        current_card = choice(to_learn)  # Seleciona aleatóriamente uma palavra
        canvas.itemconfig(card_title, text="English", fill="black")  # Configura o titulo
        canvas.itemconfig(card_word, text=current_card["English"], fill="black")  # Configura a palavra
        canvas.itemconfig(card_backgorund, image=card_front_img)  # Configura a imagem de background
        flip_timer = screen.after(3000, func=flip_card)  # Reativa o timer para mostrar a resposta
    else:
        messagebox.showinfo(title="Congratulations!!!!", message="You learned all the words!!!")
        exit()


def flip_card():
    """Tem a função de virar a carta"""

    canvas.itemconfig(card_title, text="Portuguese-BR", fill="white")
    canvas.itemconfig(card_word, text=current_card["Portuguese-BR"], fill="white")
    canvas.itemconfig(card_backgorund, image=card_back_img)


def is_know():
    """Tem como função remover a palavra do arquivo to_learn, caso o usuário já conheça a palavra"""

    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# Criando a tela
screen = Tk()
screen.title("Flashy")
screen.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
screen.minsize(width=500, height=500)

# Primeiro timer para aparecer a resposta
flip_timer = screen.after(3000, func=flip_card)  # Executa uma função após 3 segundos

# Cria o Canvas
canvas = Canvas(width=800, height=526) 
card_front_img = PhotoImage(file="images/card_front.png")  
card_back_img = PhotoImage(file="images/card_back.png")  
card_backgorund = canvas.create_image(400, 263, image=card_front_img) 
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))  
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))  
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)  
canvas.grid(row=0, column=0, columnspan=2) 

# Cria o botão vermelho de errado
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

# Cria o botã verde de acerto
check_image = PhotoImage(file="images/right.png")
know_button = Button(image=check_image, highlightthickness=0, command=is_know)
know_button.grid(row=1, column=1)

next_card()  # É executado aqui para mostrar a primeira palavra

screen.mainloop()
