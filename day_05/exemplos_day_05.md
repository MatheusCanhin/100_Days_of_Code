# Exemplos de código do dia 5

- Exemplo 1:
    Crie um código que receba diversas alturas de estudantes e retorne a média da altura de todos esses estudantes.

~~~python
student_heights = input("Input a list of student heights: ").split()

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
  total_height += height
print(f"total height = {total_height}")

number_of_students = 0
for student in student_heights:
  number_of_students += 1
print(f"number of students = {number_of_students}")
  
print(round(total_height /number_of_students))
~~~

---
- Exemplo 2:
  Crie um código que receba diversas entradas de notas de alunos, separadas por espaço, transforme esses dados em uma lista e retorne o maior valor da lista sem utilizar a função max.

~~~python
student_scores = input("Input a list of student scores ").split()

for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

highest_score = 0
for score in student_scores:
  if score > highest_score:
    highest_score = score
    
print(f"The highest score in the class is: {highest_score}")
~~~

---
- Exemplo 3:
  Crie um código que some todos os números pares de 0 a 100.
~~~python
even_sum = 0

for number in range(0, 101, 2):
  even_sum += number

print(even_sum)
~~~

---
- Exemplo 4:
  Crie o algoritmo "FizzBuzz" de 1 a 100 onde todo número que é divisivel por 3 sem sobrar nenhum resto deve printar "Fizz"
  E se o número for divísivel pr 5 devemos printar "Buzz", se o número for divisivel por ambos devemos mostrar "FizzBuzz".

~~~python
for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)
~~~