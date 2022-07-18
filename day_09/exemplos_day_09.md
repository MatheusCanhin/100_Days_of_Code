# Exemplos dia 9

- Exemplo 1:
  Basicamente neste exemplo 1 recebemos um dicionário com o nome e a nota de alguns alunos e queremos que o programa nos retorne um outro dicionário contendo o nome do aluno e uma mensagem conforme a sua nota.

~~~python
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for key, value in student_scores.items():
  if value >= 91:
    student_grades[key] = "Outstanding"
  elif value >= 81:
    student_grades[key] = "Exceeds Expectations"
  elif value >= 71:
    student_grades[key] = "Acceptable"
  else:
    student_grades[key] = "Fail"

print(student_grades)
~~~

- Exemplo 2:
  Neste exemplo queremos criar um código que adicione em uma lista de dicionários um novo valor, para isso, devemos criar uma função.

~~~python
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country, times_visited, cities):
  dictionary = {}
  dictionary['country'] = country
  dictionary['visits'] = times_visited
  dictionary['cities'] = cities

  travel_log.append(dictionary)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
~~~