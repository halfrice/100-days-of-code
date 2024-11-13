import os
import random
import sys
import time
import art


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def get_card_rank(card):
    return card[:-1]


def get_card_suit(card):
    return card[-1]


def get_card_value(card):
    values = {'J': 10, 'Q': 10, 'K': 10, 'A': 11}
    value = 0
    rank = get_card_rank(card)

    if rank in values:
        value = values[rank]
    else:
        value = int(rank)

    return value


def get_card_values(cards):
    ace_overflow = 0  # Special case for Ace values being 11 or 1
    total = 0

    for card in cards:
        card_rank = get_card_rank(card)
        card_value = get_card_value(card)

        if card_rank == 'A':
            ace_overflow += 10

        total += card_value

    while total > 21 and ace_overflow:
        ace_overflow -= 10
        total -= 10

    return total


def make_deck():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['H', 'C', 'D', 'S']
    deck = []

    for s in suits:
        for r in ranks:
            deck.append(r + s)

    random.shuffle(deck)
    return deck


def make_shoe(n_decks):
    shoe = []

    for i in range(n_decks):
        deck = make_deck()
        for card in deck:
            shoe.append(card)

    random.shuffle(shoe)
    return shoe


def add_card(hand, shoe):
    r = random.randint(0, len(shoe) - 1)
    card = shoe.pop(r)
    hand.append(card)
    return hand


def deal_hands(shoe):
    hands = []

    for i in range(2):  # 2 cards per hand
        for j in range(2):  # 2 Players (Man vs Dealer)
            if j >= len(hands):
                hands.append([])
            add_card(hands[j], shoe)

    return hands


def draw_hand(cards, hide_dealers_card=False):
    n_card_lines = art.cards['S'].split('\n')
    hand = [''] * len(n_card_lines)
    for i, card in enumerate(cards):
        rank = get_card_rank(card)
        suit = get_card_suit(card)

        # Replace placeholder rank
        if i == len(cards) - 1 and hide_dealers_card:
            card_lines = art.cards['_'].split('\n')
        else:
            card_lines = art.cards[suit].split('\n')
            rank_line = list(card_lines[1])
            for i, c in enumerate(rank):
                rank_line[i + 1] = c
            card_lines[1] = ''.join(rank_line)

        # Build the strings for the hand by lines
        for i, line in enumerate(card_lines):
            hand[i] += card_lines[i]

    print('\n'.join(hand))


def draw_hands(hands, hide_dealers_card=False):
    dealers_hand = hands[-1]
    player_hand = hands[0]

    if hide_dealers_card:
        print(f'Dealer: {get_card_value(dealers_hand[0])}')
    else:
        print(f'Dealer: {get_card_values(dealers_hand)}')

    draw_hand(dealers_hand, hide_dealers_card)
    print(f'You: {get_card_values(player_hand)}')
    draw_hand(player_hand)


def is_bust(hand):
    total = get_card_values(hand)
    if total > 21:
        return True
    return False


# Intro
print(art.logo)

user_input = input("Deal the hands? Type 'y' or 'n': ").lower()
if user_input == 'n':
    sys.exit()

# Double Deck Blackjack
num_of_decks = 2
shoe = make_shoe(num_of_decks)
starting_shoe_len = len(shoe)

wins = 0
losses = 0
pushes = 0
game_running = True

# Start game
while game_running:
    if len(shoe) < starting_shoe_len / 5:
        shoe = make_shoe(num_of_decks)
        clear_screen()
        print('The Dealer suspiciously reshuffles the deck...')
        time.sleep(2)

    hands = deal_hands(shoe)
    dealers_hand = hands[-1]
    players_hand = hands[0]

    clear_screen()
    draw_hands(hands, hide_dealers_card=True)

    # Player's turn
    dealers_turn = False
    players_turn = True

    while players_turn:
        if is_bust(players_hand):
            players_turn = False
            print('Bust...')
            break

        hit_me = input("Hit or Stay? Type 'h' or 's': ").lower()
        if hit_me == 'h':
            print('You hit...')
            add_card(players_hand, shoe)
            time.sleep(1.5)
        else:
            players_turn = False
            dealers_turn = True

        clear_screen()
        draw_hands(hands, hide_dealers_card=True)

    # Dealer's turn
    print('The dealer flips over the card...')
    time.sleep(2)
    clear_screen()
    draw_hands(hands, hide_dealers_card=False)

    while dealers_turn:
        score = get_card_values(dealers_hand)
        target_score = 17

        while score < target_score:
            print('Dealer hits...')
            add_card(dealers_hand, shoe)
            score = get_card_values(dealers_hand)
            time.sleep(1.5)
            clear_screen()
            draw_hands(hands)

        dealers_turn = False

    # Score the game
    if is_bust(players_hand):
        print('You got greedy and busted. You lose...')
        losses += 1
    elif is_bust(dealers_hand):
        print('Dealer busted! Big Money! You Win!!')
        wins += 1
    else:
        dealers_score = get_card_values(dealers_hand)
        players_score = get_card_values(players_hand)

        if players_score > dealers_score:
            print('You Win!!')
            wins += 1
        elif players_score == dealers_score:
            print('Push.')
            pushes += 1
        else:
            print('You lose...')
            losses += 1

    # Ask user if they'd like to play again
    dealer_actions = [
        'The Dealer looks at you.',
        'The Dealer raises an eyebrow in your direction.',
        "The Dealer smugly asks if you're done.",
        'The Dealer deadpans in your direction.',
        'The Dealer snickers, probably at you.',
    ]

    more = input(
        f"{random.choice(dealer_actions)}\nPlay again?' Type 'y' or 'n': "
    ).lower()
    if more == 'n':
        print(f'\nSession Record:\nWins: {wins}\nLosses: {losses}\nPushes: {pushes}\n')
        sys.exit()
