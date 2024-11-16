from sys import exit
from art import logo

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

print(logo)

on = True
while on:
    opts = menu.get_items()
    cmd = input(f'What would you like? ({opts}): ')
    if cmd == 'report':
        coffee_maker.report()
    elif cmd == 'off':
        print('Powering off. Goodbye')
        exit()
    else:
        drink = menu.find_drink(cmd)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(
            drink.cost
        ):
            coffee_maker.make_coffee(drink)
