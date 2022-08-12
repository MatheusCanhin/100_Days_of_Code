from tkinter import *

FONT = ("Arial", 10, "bold")


def convert():
    miles = float(entry1.get()) * 1.609
    label3.config(text=f"{miles:.2f}")


# Criando a tela
screen = Tk()
screen.title("Miles to Kilometer Converter")
screen.minsize(width=300, height=200)
screen.config(padx=50, pady=50)


# Criando Texto "is equal to"
label1 = Label(text="is equal to", font=FONT)
label1.grid(column=0, row=1)

# Criando Texto "Miles"
label2 = Label(text="Miles", font=FONT)
label2.grid(column=2, row=0)

# Criando Textp "Km"
label3 = Label(text="Km", font=FONT)
label3.grid(column=2, row=1)

# Criando Caixa de entrada
entry1 = Entry(width=10)
entry1.grid(column=1, row=0)


# Criando campo da resposta
label3 = Label(text='0', font=FONT)
label3.grid(column=1, row=1)

# Criando o botão
button = Button(text="Calculate", command=convert, font=FONT)
button.grid(column=1, row=2)


screen.mainloop()
