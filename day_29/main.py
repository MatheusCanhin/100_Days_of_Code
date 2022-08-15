from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    """Cria uma senha aleatória e passa ela para o nosso Ctrl+V"""

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Cria listas aleatórias de letras, números e simbolos
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    # Adiciona todas as listas de caracteres em uma só e embaralha
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    # Junta a senha, escreve no campo password e salva no nosso Ctrl+V
    password_join = ''.join(password_list)
    password_entry.insert(0, password_join)
    pyperclip.copy(password_join)  # Podemos utilizar automaticamento com o Ctrl+V

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    """Adiciona o site, o email e a senha criada no arquivo TXT"""

    # Pega todos os textos das entradas
    website_text = website_entry.get()
    email_text = email_entry.get()
    password_text = password_entry.get()

    # Verifica o tamanho de cada entrada, se algum for 0, mostra um pop-up
    if len(website_text) == 0 or len(password_text) == 0 or len(email_text) == 0:
        messagebox.showinfo(title="OPS!!!", message="Plesa make sure you haven't left any fields empty")
    else:
        # Faz com que o usuário confirme os valores
        is_ok = messagebox.askokcancel(title=website_text, message=f"Details entered:\nEmail: {email_text}"
                                                                   f"\nPassowrd: {password_text}\nIs it ok to save?")
        # Se os valores forem confirmados adiciona os dados no arquivo txt, e limpa os campos da senha e website
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website_text} | {email_text} | {password_text}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

# Criando a tela
screen = Tk()
screen.title("Password Manager")
screen.configure(width=240, height=240, pady=20, padx=20)

# Criando Canva
canvas = Canvas(width=200, height=200, highlightthickness=0)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)


# LABELS
# Criando a label website
website = Label(text="Website:", font=("Arial", 10, "bold"))
website.grid(column=0, row=1)

# Criando a label email
email = Label(text="Email/Username:", font=("Arial", 10, "bold"))
email.grid(column=0, row=2)

# Criando a label Password
password = Label(text="Password:", font=("Arial", 10, "bold"))
password.grid(column=0, row=3)


# ENTRY
# Criando o campo para digitar o website
website_entry = Entry(width=50)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

# Criando o campo para digitar o email
email_entry = Entry(width=50)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "exemplo_email@gmail.com")

# Criando o campo para digitar a senha
password_entry = Entry(width=34)
password_entry.grid(column=1, row=3)


# BOTÕES
# Criando botão que gera senha
botao_senha = Button(text="Generate Password", font=("arial", 7, "bold"), command=generate_password)
botao_senha.grid(column=2, row=3)

# Criando botão ADD
botao_add = Button(text="Add", width=42, command=save)
botao_add.grid(column=1, row=4, columnspan=2)

screen.mainloop()
