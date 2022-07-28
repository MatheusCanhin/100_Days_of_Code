MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
COINS = {'Pennies': 0.01,
         'Nickels': 0.05,
         'Dimes': 0.10,
         'Quarters': 0.25}
money = 0


def main():
    """Start the program"""
    while True:
        user = input("What would you like? (espresso/latte/cappuccino): ").strip().lower()
        if user in MENU.keys():
            if check_resources(user):
                if process_coins(user):
                    make_coffee(user)

        elif user == 'report':
            report()
        elif user == 'off':
            print("The machine is shutting down")
            break
        else:
            print('Please enter an acceptable value')


def report():
    """Print all the resources in the machine"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def check_resources(item):
    """Check if are enough resources"""
    drink = MENU[item]['ingredients']
    for key, value in drink.items():
        if value > resources[key]:
            print(f'Can´t do the {item}, we have less {key} than necessary')
            return False
    return True


def process_coins(item):
    """Verify the amount of coins"""
    global money
    total = 0
    cost = MENU[item]['cost']
    print('Please insert the coins')
    for coin, value in COINS.items():
        a = float(input(f'How many {coin}? ')) * value
        total += a
    if total >= cost:
        money += cost
        print(f'Your money change is ${round(total-cost,2)}')
        return True

    else:
        print(f"The money is not enough, the {item} costs ${cost}, you inserted a total of ${round(total,2)}.")
        print("Money refunded")
        return False


def make_coffee(item):
    """Make the coffee"""
    global resources, MENU
    drink = MENU[item]['ingredients']
    for key, value in drink.items():
        resources[key] -= MENU[item]['ingredients'][key]
    print(f'Your {item} is ready, enjoy it!!!')


if __name__ == '__main__':
    main()
