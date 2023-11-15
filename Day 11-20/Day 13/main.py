# Higher or Lower

# 1. Import the required librairies
import random
import time
import os

# 2. Declare the require variables
from game_data import data

logo = '''

██   ██ ██  ██████  ██   ██ ███████ ██████       ██████  ██████      ██       ██████  ██     ██ ███████ ██████  
██   ██ ██ ██       ██   ██ ██      ██   ██     ██    ██ ██   ██     ██      ██    ██ ██     ██ ██      ██   ██ 
███████ ██ ██   ███ ███████ █████   ██████      ██    ██ ██████      ██      ██    ██ ██  █  ██ █████   ██████  
██   ██ ██ ██    ██ ██   ██ ██      ██   ██     ██    ██ ██   ██     ██      ██    ██ ██ ███ ██ ██      ██   ██ 
██   ██ ██  ██████  ██   ██ ███████ ██   ██      ██████  ██   ██     ███████  ██████   ███ ███  ███████ ██   ██ 
                                                                                                                
                                                                                                                

                                                                                           
'''
vs = '''
██╗   ██╗███████╗
██║   ██║██╔════╝
██║   ██║███████╗
╚██╗ ██╔╝╚════██║
 ╚████╔╝ ███████║
  ╚═══╝  ╚══════╝
                 

'''


# 3. Define the functions needed


def clear(seconds=0):
    time.sleep(seconds)
    # Use 'cls' for Windows and 'clear' for Unix-like systems
    os.system('cls' if os.name == 'nt' else 'clear')


def get_account():
    return random.choice(data)


def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return (f"{name}, a {description}, from {country}.")


def check_answer(account_a, account_b, guess):
    if account_a > account_b:
        return guess == "a"
    else:
        return guess == "b"


def game_loop():
    print(logo)
    score = 0
    continue_game = True
    account_a = get_account()
    account_b = get_account()

    while continue_game:
        account_a = account_b
        account_b = get_account()

        while account_a == account_b:
            account_b = get_account()

        print(f"Compare A: {format_data(account_a)}")
        print(vs)
        print(f"Compare B: {format_data(account_b)}")

        guess = input("Who has more followers? Type A or B: ").lower()
        follower_a = account_a["follower_count"]
        follower_b = account_b["follower_count"]

        clear()
        print(logo)
        if check_answer(follower_a, follower_b, guess):
            score += 1
            print(
                f"\nCorrect! The answer is {guess}!\nYour current score is {score}.")
        else:
            continue_game = False
            print(f"\nIncorrect! Your final score is {score}.")


# 4. Run the game loop
game_loop()
