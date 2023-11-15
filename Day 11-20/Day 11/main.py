# Guess the number

# 1. Import the libraries
import random

# 2. Declare the variables

logo = '''
   _____ _    _ ______  _____ _____   _______ _    _ ______   _   _ _    _ __  __ ____  ______ _____  
  / ____| |  | |  ____|/ ____/ ____| |__   __| |  | |  ____| | \ | | |  | |  \/  |  _ \|  ____|  __ \ 
 | |  __| |  | | |__  | (___| (___      | |  | |__| | |__    |  \| | |  | | \  / | |_) | |__  | |__) |
 | | |_ | |  | |  __|  \___ \\___  \\     | |  |  __  |  __|   | . ` | |  | | |\/| |  _ <|  __| |  _  / 
 | |__| | |__| | |____ ____) |___) |    | |  | |  | | |____  | |\  | |__| | |  | | |_) | |____| | \ \ 
  \_____|\____/|______|_____/_____/     |_|  |_|  |_|______| |_| \_|\____/|_|  |_|____/|______|_|  \_\\
'''

# 3. Create a function that will generate and print the secret number between 0 and 100

EASY = 10
HARD = 5


def generate_secret():
    global secretNumber
    secretNumber = random.randint(0, 100)
    return secretNumber


def set_difficulty():
    level = input("Choose difficulty, easy or hard: ")
    if level == 'easy':
        return EASY
    elif level == 'hard':
        return HARD


def check_answer():
    global LIVES  # Use the global keyword to modify the global variable
    global GUESS
    while LIVES > 0:
        GUESS = int(input("Make a guess: "))
        if GUESS == secretNumber:
            print(
                f'\nCongratulations! You got it right, the answer was {secretNumber}')
            print(f"You did it with {LIVES} lives left")
            break  # Exit the loop if the correct number is guessed
        elif GUESS > secretNumber:
            print("Too high! Try again.")
        elif GUESS < secretNumber:
            print("Too low! Try again.")
        LIVES -= 1
        print(f"\nCurrent lives left: {LIVES}")
    else:
        print(
            f"\nSorry, you ran out of lives. The correct answer was {secretNumber}")


print(logo)
print("\nWelcome to the Number Guessing Game!")
print("I am thinking of a number between 0 and 100")
turns = set_difficulty()
LIVES = turns
# Initialize LIVES with the difficulty level
print(f"\nYou have {LIVES} attempts to guess the answer.")
generate_secret()
check_answer()
