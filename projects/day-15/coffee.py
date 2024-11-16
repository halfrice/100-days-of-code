import sys
import art


def print_report(resources):
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']:.2f}\n")


def get_input(s, type):
    while True:
        try:
            return type(input(s))
        except ValueError:
            print('Invalid input. Try again.')


def check_resources(ingredients, resources):
    for i, n in ingredients.items():
        if i in resources:
            if n > resources[i]:
                print(f'Sorry there is not enough {i}.')
                return False
        else:
            return False
    return True


def process_coins(cost, resources):
    # coin_types and coin_values have respective indexes
    coin_types = ['quarters', 'dimes', 'nickles', 'pennies']
    coin_values = [0.25, 0.1, 0.05, 0.01]
    coins = []
    total = 0

    # Get coins
    print(f'The amount due is: ${cost:.2f}.')
    print('Please insert coins.')
    for i, c in enumerate(coin_types):
        while True:
            coins_input = get_input(f'How many {c}?: ', int)
            if coins_input < 0:
                print('Trying to hack me bro? Only positive integers allowed.')
                continue
            break

        coins.append(coins_input)
        total += coins_input * coin_values[i]

    # Process coins
    if total >= cost:
        resources['money'] += cost
        change = total - cost

        if change:
            print(f'Here is ${change:.2f} in change.\n')
        return True
    else:
        print(f'Error. Refunding ${total:.2f}')
    return False


MENU = {
    'coffee': {
        'ingredients': {
            'water': 300,
            'coffee': 75,
        },
        'cost': 1.25,
    },
    'espresso': {
        'ingredients': {
            'water': 50,
            'coffee': 18,
        },
        'cost': 1.5,
    },
    'latte': {
        'ingredients': {
            'water': 200,
            'milk': 150,
            'coffee': 24,
        },
        'cost': 2.5,
    },
    'cappuccino': {
        'ingredients': {
            'water': 250,
            'milk': 100,
            'coffee': 24,
        },
        'cost': 3.0,
    },
}

resources = {
    'water': 300,
    'milk': 200,
    'coffee': 100,
    'money': 0,
}

# Intro
print(art.logo)

on = True
while on:
    drink_types = []
    for d in MENU.keys():
        drink_types.append(d)

    cmd = get_input(f'What would you like? ({'/'.join(drink_types)}): ', str).lower()
    if cmd in drink_types:
        drink = cmd
        enough_res = check_resources(MENU[drink]['ingredients'], resources)
        if enough_res:
            enough_money = process_coins(MENU[drink]['cost'], resources)
            if enough_money:
                print(f'Here is your {drink} ☕️ Enjoy!\n')
    elif cmd == 'report':
        print_report(resources)
    elif cmd == 'off':
        print('Powering off. Goodbye.')
        sys.exit()
