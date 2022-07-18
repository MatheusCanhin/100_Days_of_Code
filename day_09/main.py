from replit import clear
from art import logo

bids = {}
bidding_finished = False

def max_bid(bids_values):
    winner = max(bids_values, key = lambda chave: bids_values[chave])
    print(f"The winner is {winner} with a bid of ${bids_values[winner]}")


while not bidding_finished:

    print(logo)
    name = input("What's your name? ")
    price = float(input("What's your bid? $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. ")

    if should_continue == 'no':
        bidding_finished = True
        max_bid(bids)
    elif should_continue == 'yes':
        clear()