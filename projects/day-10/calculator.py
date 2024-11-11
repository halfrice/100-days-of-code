import os
import art


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# Intro
clear_screen()
print(art.calculator)
print('Welcome to Calculator')

operations = {'+': add, '-': subtract, '*': multiply, '/': divide}
result = 0
first_run = True
calculating = True
while calculating:
    if first_run:
        n1 = float(input("What's the first number?: "))
    else:
        n1 = result
    for o in operations:
        print(o)
    op = ''
    while op not in operations:
        op = input('Pick an operation: ')
    n2 = float(input("What's the next number?: "))

    result = operations[op](n1, n2)
    print(f'{n1} {op} {n2} = {result}')

    keep_calculating = input(
        f"Type 'y' to continue calculating with {result}, type 'n' to start a new calculation: "
    ).lower()
    if keep_calculating == 'y':
        first_run = False
    else:
        first_run = True
        clear_screen()
