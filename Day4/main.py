# Rock, paper, scissors game

# Import the required libraries
import random

# 1. Initialize the rock, paper, and scissors ASCII code


def rock_paper_scissors():
    rock = '''
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
            ______)
            _______)
            _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    '''

    game_images = [rock, paper, scissors]

    # 2. Print a greeting message
    while True:
        print('\n************** Welcome to the Rock, Papers, Scissors Game **************')

        # 3. Get user input for their choice of either rock, paper, or scissors
        while True:
            try:
                choice = int(input(
                    '\nWhat hand do you want to play, rock (press 0), paper (press 1), scissors (press 2)?: '))
                choices_dict = {0: 'rock', 1: 'paper', 2: 'scissors'}

                if choice in choices_dict:
                    print(f'You chose: {choices_dict[choice]}')
                    print(game_images[choice])
                    break  # Exit the inner loop if a valid choice is provided
                else:
                    print(
                        "Please select a valid choice (0 for rock, 1 for paper, or 2 for scissors)!")
            except ValueError:
                print("\nInvalid input. Please enter a number.")

        # Generate computer's choice only if the user provides a valid input
        computer_choice = random.randint(0, 2)
        print(f'Computer chose: {choices_dict[computer_choice]}')
        print(game_images[computer_choice])

        computer_win = "The computer won!"
        player_win = "The player won!"

        # 4. Define logic for who wins and loses
        if computer_choice == 0 and choice == 1:
            print(player_win)
        elif computer_choice == 0 and choice == 2:
            print(computer_win)
        elif computer_choice == 1 and choice == 0:
            print(computer_win)
        elif computer_choice == 1 and choice == 2:
            print(player_win)
        elif computer_choice == 2 and choice == 0:
            print(player_win)
        elif computer_choice == 2 and choice == 1:
            print(computer_win)
        elif computer_choice == choice:
            print("It's a tie!")
        else:
            print("Unexpected outcome. Something went wrong!")

        play_again = input(
            "\nDo you want to play again? Press y for yes or n for no?: ")
        if play_again.lower() != 'y':
            print("Thank you for playing Rock, Paper, Scissors!")
            break


rock_paper_scissors()
