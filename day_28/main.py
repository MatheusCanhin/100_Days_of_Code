from tkinter import *
from math import floor
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    """Tem a função de resetar o contador, as REPS, remover o checkmark e mudar o titulo para Timer"""
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label1.config(text="Timer", fg=GREEN)
    label2.config(text="")
    global REPS
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    """Tem a função de iniciar o TIMER"""
    global REPS
    REPS += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        label1.config(text="Break", fg=RED)
        count_down(long_break_sec)

    elif REPS % 2 == 0:
        label1.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        label1.config(text="Work", fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    """Realiza a contagem regressiva"""

    count_min = floor(count / 60)  # quantidade de minutos
    count_sec = count % 60  # quantidade de segundos

    # if para mostrar o valor com um 0 na frente quando menor que zero
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")  # modifica o timer_text

    # Verifica o valor da contagem
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        work_sessions = floor(REPS/2)
        for _ in range(work_sessions):
            mark += "✔"
        label2.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
# Criando a tela


window = Tk()
window.title("Pomodoro")  # Cria o título da janela
window.config(padx=100, pady=50, bg=YELLOW)  # Cria e configura cor e tamanho da janela


# Criando canva
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)  # define tamanho, back e remove a linha do canva
photo = PhotoImage(file="tomato.png")  # Adiciona a imagem a ser utilizada
canvas.create_image(100, 112, image=photo)  # Cria a imagem
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 27, "bold"))  # Cria o texto no canva
canvas.grid(column=1, row=1)  # Faz o canva aparecer na tela


# Criando a palavra Timer
label1 = Label(text="Timer", font=(FONT_NAME, 50, "bold"), bg=YELLOW, fg=GREEN)
label1.grid(column=1, row=0)

# Criando o botão start
botao_start = Button(text="Start", highlightthickness=0, command=start_timer)
botao_start.grid(column=0, row=2)

# Criando o botão reset
botao_reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
botao_reset.grid(column=2, row=2)

# Criando o checkmark
label2 = Label(bg=YELLOW, fg=GREEN)
label2.grid(column=1, row=3)

window.mainloop()