# Caesar Cipher

# 1. Import the required code from the constants file
from constants import alphabet, logo

# Create a function for Caesar Cipher
def caesar_cipher(direction, message, shift):
    result_text = ""
    position = 0
    for letter in message:
        if letter in alphabet:
            if direction == 'encode':
                position = alphabet.index(letter) + shift
            elif direction == 'decode':
                position = alphabet.index(letter) - shift

            new_position = position % 26
            new_letter = alphabet[new_position]
            result_text += new_letter
        else:
            result_text += letter
    
    if direction == 'encode':
        print(f'The encoded message is: {result_text}')
    elif direction == 'decode':
        print(f'The decoded message is: {result_text}')

# Initialize the text variable before the while loop
text = ""

# Start the while loop
while True:
    print(logo)

    direction = input("Type encode for message encoding, and decode for message decoding: ")

    # Check if the entered direction is valid
    if direction != 'encode' and direction != 'decode':
        print('Invalid option! Please type either encode or decode.')
    else:
        shift_number = int(input("Enter a shift number (0-25): "))
        text = input("Enter your message: ").lower()

        caesar_cipher(direction, text, shift_number)

    another_message = input("Do you want to encode/decode another message? (yes/no): ").lower()

    if another_message != 'yes':
        print("Thank you for using the Caesar Cipher!")
        break  # Exit the loop if the user enters anything other than 'yes'
