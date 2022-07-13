# Exemplos que foram criados no dia 4

- 1° Exemplo:
 
    Criar um jogo que mostra "Heads ou Tails" a partir de um número sorteado pelo programa (0 ou 1)

~~~python
from random import randint

valor = randint(0,1)

if valor == 0:
  print('Heads')
else:
  print('Tails')
~~~

- Exemplo 2:
  
  Crie um programa que recebe diversos nomes separados por vírgula, realize o split desses nomes, transformando-os em uma lista, e assim faça o sorteio de quem deve pagar a conta.

  You are going to write a program which will select a random name from a list of names. The person selected will have to pay for everybody's food bill. 

  **Important**: You are not allowed to use the `choice()` function.

~~~python
from random import randint, choice

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

random_name = randint(0, len(names) - 1)
print(f"{names[random_name]} is going to buy the meal today!")

# with choice
choice_name = choice(names)
print(f"{choice_name} is going to buy the meal today!")
~~~

- Exemplo 3:

    Criar um código que mostre uma matriz e solicite que o usuário digite o número da linha e coluna, com o objetivo desse input ser o local que a pessoa vai guardar um tesouro.
    Your job is to write a program that allows you to mark a square on the map using a two-digit system. The first digit is the vertical column number and the second digit is the horizontal row number. e.g.:

    First your program must take the user input and convert it to a usable format. 

    Next, you need to use it to update your nested list with an "x". 

~~~python
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")
line = int(position[0])
column = int(position[1])

map[line-1][column-1] = "X"

print(f"{row1}\n{row2}\n{row3}")
~~~