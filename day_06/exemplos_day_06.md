# Exemplos do dia 6
Os exemplos desse sexto dia são todos relacionados ao **Reeborg's World** 
- Exemplo 1:
  Para este exemplo vamos criar um código utilizando o for que satisfaça o [Reeborg's World](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json)
~~~python
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
 
for i in range(6):
    jump()
~~~

- Exemplo 2:
  Para este exemplo devemos criar um programa com o loop while que satisfaça o puzzle do seguinte level [Reeborg's World](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json)

~~~python
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
 
while not at_goal():
    jump()
~~~

- Exemplo 3:
  Para este exemplo devemos criar um programa com o loop while que satisfaça o puzzle do seguinte level [Reeborg's World](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json)

~~~python
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()
 
while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()
~~~

- Exemplo 4:
  Para este exemplo devemos criar um programa com o loop while que satisfaça o puzzle do seguinte level [Reeborg's World](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json)

~~~python
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    while wall_on_right():
        move()

    turn_right()
    move()
    turn_right()

    while not wall_in_front():
        move()
    turn_left()
 
while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()
~~~