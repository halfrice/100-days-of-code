import os
from art import gavel


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def find_highest_bidder(bids):
    winner = ''
    high = 0

    for bidder in bids:
        bid = bids[bidder]
        if bid > high:
            high = bid
            winner = bidder

    return (winner, high)


# Intro
clear_screen()
print(gavel)
print('Welcome to Secret Auction (Drop the "the". It\'s clean)')

bids = {}
bidding = True
while bidding:
    name = input('What is your name?\n')
    price = int(input('What is your bid?\n$'))
    bids[name] = price

    keep_bidding = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
    if keep_bidding == 'no':
        winner, bid = find_highest_bidder(bids)
        print(f'The highest bidder is {winner} with a bid of ${bid}')
        bidding = False
    else:
        clear_screen()
