import os
import random
import sys
import art
import game_data


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def format_item(item):
    name = item['name']
    desc = item['description']
    country = item['country']
    return f'{name}, a {desc}, from {country}'


def get_item(data):
    r = random.randint(0, len(data) - 1)
    item = data.pop(r)
    return item


def get_most_popular(a, b):
    a_popularity = a['follower_count']
    b_popularity = b['follower_count']
    if a_popularity > b_popularity:
        return 'a'
    elif b_popularity > a_popularity:
        return 'b'
    else:
        return 't'  # in case of a tie, both answers will be treated as correct


def play_round(a, b):
    print(f'Compare A: {format_item(a)}')
    print(art.vs)
    print(f'Compare B: {format_item(b)}\n')
    answer = input("Who has more followers? 'A' or 'B': ").lower()

    most_popular = get_most_popular(a, b)
    if answer == most_popular:
        return True
    elif most_popular == 't' and (answer == 'a' or answer == 'b'):  # handle tie case
        return True

    return False


def play_game():
    data = game_data.data
    prev_score = -1
    score = 0
    a = {}
    b = get_item(data)

    # Game loop
    while True:
        while not a:
            a = b
            b = get_item(data)

        clear_screen()
        print(f'{art.logo}')
        if score and score > prev_score:
            print(f"You're right! Current score: {score}\n")
        elif score == prev_score:
            print(f"Sorry, that's wrong. Final score: {score}")
            break

        correct = play_round(a, b)
        prev_score = score
        if correct:
            score += 1
            a = {}


# App loop
while True:
    play_game()

    more = input("Play again? Type 'y' or 'n': ").lower()
    if more == 'n':
        sys.exit()
