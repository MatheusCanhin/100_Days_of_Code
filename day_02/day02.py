#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#Write your code below this line 👇


# Welcome
print('Welcome to the tip calculator.')

# Getting the value of the bill
bill = float(input('What was the total bill? $'))

# Getting the tip
tip = int(input('What percentage tip would you like to give? 10, 12, or 15? '))

# Getting how many people will pay the bill
people = int(input('How many people to split the bill? '))

equation = (bill/people) * (1 + (tip/100))

print(f'Each person should pay: ${round(equation, 2):.2f}') 