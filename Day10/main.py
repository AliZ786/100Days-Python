# Blackjack

# 1.Import the required libraries
import random
import os
import time

# 2. Declare required variables
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
print(logo)


def clear(seconds=0):
    time.sleep(seconds)
    # Use 'cls' for Windows and 'clear' for Unix-like systems
    os.system('cls' if os.name == 'nt' else 'clear')


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw! 🪢"
    elif user_score > 21:
        return "You Lose! You went over 21.🥲"
    elif computer_score > 21:
        return "Computer Busted! You win.😁"
    elif computer_score == 0:
        return "Opponent has a blackjack. You lose.🥹"
    elif user_score == 0:
        return "Blackjack! You win!🎉"
    elif user_score > computer_score:
        return "You won. 🥂"
    else:
        return "You lose. 😔"


def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(
            f"Your cards are: {user_cards}, and current score is {user_score}.")
        print(f"Computers first card is {computer_cards[0]}.")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_deal = input("Type y to get another card, type n to pass: ")
            if user_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(
        f'Your final hand is {user_cards}, and your final score {user_score}.')
    print(
        f'The computers final hand is {computer_cards}, and the final score {computer_score}.')
    print(compare(user_score, computer_score))


while (input("\nDo you want to play a game of blackjack. Press y for yes and n for no?: ")) == 'y':
    clear()
    play_game()
