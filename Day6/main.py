# Hangman game

# 1. Import required librairies
import random
from hangman_words import word_list


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

print(logo)

# 2. Chose a word from the list at random
lives = 6
random_word = random.choice(word_list)


# 3. Create the number of blanks depending on the length of the word chosen
display = []
for letter in range(len(random_word)):
    display += "_"

end_of_game = False
guessed_letters = set()


# 4. Ask the user to guess a letter in the word
while not end_of_game:
    guess = input("Guess a letter: ").lower()


# 5. Check through the chosen word and see letter by letter if it was correct or not

# Check if the letter is already been guessed
    if guess in guessed_letters:
        print("You've already guessed that letter!")
        continue
    guessed_letters.add(guess)

    for position in range(len(random_word)):
        letter = random_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in random_word:
        lives -= 1
        print('Wrong! You have {} lives left'.format(lives))
        if lives == 0:
            end_of_game = True
            print("You lose!")
            print(f'The word was: {random_word}')

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You have won!")

# 6. Print the stage of lives to be decreased with every wrong answer
    print(stages[lives])
