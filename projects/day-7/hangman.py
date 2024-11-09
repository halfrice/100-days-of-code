import random
import string

import art
import words

# Words of affirmation / negation
success = [
    'Correct!',
    'Good guess!',
    'Nice!',
    'Got it!',
    'Smart!',
    'Outstanding!',
]
fail = [
    'Fail...',
    'Disappointed in you...',
    "C'mon man!",
    'Wrong...',
    "That's not it, dummy.",
    "Don't be stupid.",
]

# User lives
lives = 6
# Track of users valid guesses
used_letters = []

# Pick a random word from words list
secret_word = random.choice(words.words).upper()

# Create word cipher and fill with underscores
cipher = []
for c in secret_word:
    cipher.append('_')

# Intro
print('\n Welcome to')
print('H _ N G M _ N')
print(art.hangman[6 - lives])
print(f'{' ' * 4}\u2764 x {str(lives)}')
print(f'{' '.join(cipher)} <--Your word to guess')

# Game loop
while True:
    # Check if user has won or lost
    score = 0
    for c in cipher:
        if c != '_':
            score += 1
    if score == len(secret_word):
        print(f'You guessed the word: {secret_word}\nYou Win!!')
        break
    elif lives == 0:
        print(f'You have no lives left. You lose.\nThe word was: {secret_word}')
        break

    # Prompt user for their guess
    if used_letters:
        print(f'Used letters: {' '.join(c for c in used_letters)}')
    guess = input('Guess a letter: ').upper()

    # Evaluate users guess
    # Check if guess is a single letter and an alpha char
    if len(guess) == 1 and guess in string.ascii_uppercase:
        # Check if guess hasn't been attempted yet
        if guess not in used_letters:
            used_letters.append(guess)
            # Check if guess exists within the secret word
            if guess in secret_word:
                # Update underscores in cipher with correctly guessed letter
                for i, c in enumerate(secret_word):
                    if c == guess:
                        cipher[i] = guess
                print(random.choice(success))
            else:
                lives -= 1
                print(random.choice(fail))
        else:
            print('You already guessed that. Try again.\n')
            continue
    else:
        print('Invalid guess. Only letters a-z or A-Z are allowed. Try again.\n')
        continue

    # Draw hangman and game state
    print(art.hangman[6 - lives])
    print(f'{' ' * 4}\u2764 x {str(lives)}')
    print(f'{' '.join(cipher)}')
