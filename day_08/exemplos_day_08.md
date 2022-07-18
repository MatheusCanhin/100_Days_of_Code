# Exemplos criados no dia 8 de código.

- Exemplo 1:
  Devemos criar um código que recebe a largura e a altura de uma parede e esse programa nos retorne a quantidade de latas de tinta que serão necessárias para pintar a parede (cada lata tem a capacidade de pintar 5 m², caso o número seja quebrado devemos arredondar para cima).

  OBS: Devemos utilizar função com parâmetros.

~~~python
from math import ceil

# Defining the function 
def paint_calc(height, width, cover):
  area = (height * width) / cover
  cans = ceil(area)
  print(f"You'll need {cans} cans of paint.")

# Getting the variables and calling the function
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
~~~

- Exemplo 2:
  O segundo exemplo que teremos que desenvolver é um código que indica se um número é primo ou não, devemos utilizar função com parâmetros.
  
~~~python
# Defining the function 
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

# Getting the variables and calling the function
n = int(input("Check this number: "))
prime_checker(number=n)
~~~