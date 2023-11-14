# Auction House

# 1. Import the variables
import os
import time

# 2. Declare the variables

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)


def clear(seconds=0):
    time.sleep(seconds)
    # Use 'cls' for Windows and 'clear' for Unix-like systems
    os.system('cls' if os.name == 'nt' else 'clear')


def find_highest_bidder(bid):
    highest_bid = 0
    winner = ""
    for bidder in bid:
        bid_amt = bid[bidder]
        if bid_amt > highest_bid:
            highest_bid = bid_amt
            winner = bidder
    print(f'The winner is {winner} with the highest bid of {highest_bid}$.')


bids = {}
bidding_finished = False

while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your price?: $"))
    bids[name] = price
    continue_auction = input('Do you want to continue? (yes/no): ')
    if continue_auction == 'no':
        bidding_finished = True
        break
        find_highest_bidder(bids)
    elif continue_auction == 'yes':
        clear()
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'. Try again.")
        # Clear screen before printing out the final result
        find_highest_bidder(bids)
        break
