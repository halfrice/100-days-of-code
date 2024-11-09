import random

rock = """  ,--.--._
-" _, \\___)
   / _/____)
   \\//(____)
-\\     (__)
  `-----"
"""
paper = """   _.-._
  | | | |_
  | | | | |
  | | | | |
_ |  '-._ |
\\`\\`-.'-._;
 \\    '   |
  \\  .`  /
"""
scissors = """  .-.  _
  | | / )
  | |/ /
 _|__ /_
/ __)-' )
\\  `(.-')
 > ._>-'
"""

print('Rock Paper Scissors')
user_choice = int(
    input('What do you pick?\n' 'Type 1 for Rock, 2 for Paper, 3 for Scissors:\n')
)
computer_choice = random.randint(1, 3)

print('\nYou:')
if user_choice == 1:
    print(rock)
    print('Computer:')
    if computer_choice == 1:
        print(rock)
        print("An unstoppable force meets an immovable object.\nIt's a draw.")
    elif computer_choice == 2:
        print(paper)
        print('Paper chokes you out like a world class jiu-jitsu champion.\nYou lose.')
    elif computer_choice == 3:
        print(scissors)
        print(
            'You break the pair of scissors into pieces.'
            'There is no last resort.\n'
            'You Win!!'
        )
    else:
        print('Invalid choice.\nYou somehow lose.')
elif user_choice == 2:
    print(paper)
    print('Computer:')
    if computer_choice == 1:
        print(rock)
        print('You suffocate the rock into a lifeless husk, which it is.\n' 'You Win!!')
    elif computer_choice == 2:
        print(paper)
        print(
            'Two papers collide and create a stack, becoming post-it notes that sit on '
            'a shelf at your local Staples, unsold for eternity.\n'
            "It's a draw"
        )
    elif computer_choice == 3:
        print(scissors)
        print(
            'You get cut up like a tomato and thrown into the recycle bin.\nYou lose.'
        )
elif user_choice == 3:
    print(scissors)
    print('Computer:')
    if computer_choice == 1:
        print(rock)
        print('The rock breaks your scissors apart like a wishbone.\nYou lose.')
    elif computer_choice == 2:
        print(paper)
        print(
            "They didn't know you studied the way of the blade.\n"
            'You cut through the paper like a Samurai through a malnourished peasant.\n'
            'You Win!'
        )
    elif computer_choice == 3:
        print(scissors)
        print(
            'Two scissors attack, creating a galactic vortex of possible sex jokes.\n'
            "It's a draw."
        )
else:
    print("You've made an invalid choice.\nYou still lose.")
