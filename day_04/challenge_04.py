from random import choice

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_choices = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer = choice(game_choices)

if user_choice >= 3 or user_choice < 0:
    print('You typed an invalid number, you lose!')
else:
    user = game_choices[user_choice]

    print(f"You selected:")
    print(user)
    print(f"Computer selected:")
    print(computer)
    
    if(user == scissors and computer == paper) or (user == rock and computer == scissors) or (user == paper and computer == rock):
        print('You win!')
    elif user == computer:
        print('It´s a draw')
    else:
        print('You lose!')
