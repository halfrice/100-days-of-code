intro = '''
                  ~.
           Ya...___|__..ab.     .   .
            Y88b  \\88b  \\88b   (     )
             Y88b  :88b  :88b   `.oo'
             :888  |888  |888  ( (`-'
    .---.    d88P  ;88P  ;88P   `.`.
   / .-._)  d8P-"""|"""'-Y8P      `.`.
  ( (`._) .-.  .-. |.-.  .-.  .-.   ) )
   \\ `---( O )( O )( O )( O )( O )-' /
    `.    `-'  `-'  `-'  `-'  `-'  .' 
      `---------------------------'

            Treasure Island
Your quest is to find the treasure. Good luck!
'''

print(intro)

choice1 = input(
    "There's a split in the road ahead.\n"
    'Which direction do you choose?\n'
    'Type "left" or "right".\n'
).lower()
if choice1 == 'left':
    choice2 = input(
        '\nYou arrive at the shore of a lake.\n'
        'There is an island in the middle of the lake.\n'
        "You can't resist the temptation to go to it.\n"
        'Type "swim" to swim across.\n'
        'Type "wait" to wait for a boat.\n'
    ).lower()
    if choice2 == 'wait':
        choice3 = input(
            '\nYou trudge yourself onto the beach of the island\n'
            'You glint through the brush a big house with three doors.\n'
            'The doors are colored red, yellow, and blue.\n'
            'Which color do you choose?\n'
        ).lower()
        if choice3 == 'yellow':
            print('\nTreasure aquired!\nYou Win!!')
        else:
            if choice3 == 'red':
                print('\nYou burn alive horrifically in a room full of fire.')
            elif choice3 == 'blue':
                print('\nYou become dinner for a room full of beasts.')
            else:
                print('\nYou enter the void for eternity and go mad.')
            print('Game Over.')
    else:
        print('\nA single half-pound level 99 angry trout destroys you.\nGame Over.')
else:
    print('\nYou fall into a deep hole.\nGame Over.')
