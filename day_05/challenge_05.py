#Como desafio no final do dia foi criado um algoritmo que gera um tipo de senha aleatória,
#para isso foi utilizada a função `choice` do módulo `random` e o método `join` para juntarmos os elementos de uma lista.

from random import choice, shuffle

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = int(input('How many letters do you wnat in your password: '))
nr_numbers = int(input('How many numbers do you wnat in your password: '))
nr_symbols = int(input('How many symbols do you wnat in your password: '))

password = []
for letter in range(0, nr_letters):
    password.append(choice(letters))

for letter in range(0, nr_numbers):
    password.append(choice(numbers))

for letter in range(0, nr_symbols):
    password.append(choice(symbols))

shuffle(password)

print(''.join(password))
