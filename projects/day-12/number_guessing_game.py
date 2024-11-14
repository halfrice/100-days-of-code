import random
import sys
import art


def is_possible_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


print(art.logo)
print('Welcome to the Number Guessing Game!')

game_running = True

while game_running:
    secret_num = random.randint(1, 100)
    num_of_guesses = 0

    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == 'easy':
        num_of_guesses = 10
    else:
        num_of_guesses = 5

    while num_of_guesses > 0:
        print(f'You have {num_of_guesses} attempts remaining to guess the number.')
        guess = input('Make a guess: ')

        if is_possible_int(guess):
            guess = int(guess)
            if guess > secret_num:
                print('Too high.')
            elif guess < secret_num:
                print('Too low.')
            elif guess == secret_num:
                print(f'You got it! The answer was {secret_num}')
                break
        else:
            print('Guess again.')

        num_of_guesses -= 1
        if num_of_guesses == 0:
            print("You've run out of guesses. You lose.")
            print(f'The secret number was {secret_num}')

    more = input("Play Again? Type 'y' or 'n': ").lower()
    if more == 'n':
        print('Bye.')
        game_running = False
