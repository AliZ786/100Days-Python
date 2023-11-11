# Password Generator

# 1. Import required librairies
import random

# 2. Add greeing message
print("------ Welcome to the password generator! ------")

# 3. Ask user for input on how long they want their password to be
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '@', '*', '+']

password = []

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# 3. Generate the password based on given inputs

for char in range(1, nr_numbers+1):
    number = random.choice(numbers)
    password.append(number)

for char in range(1, nr_letters+1):
    letter = random.choice(letters)
    password.append(letter)

for char in range(1, nr_symbols+1):
    symbol = random.choice(symbols)
    password.append(symbol)


# 4. Shuffle the generated password and print it
random.shuffle(password)
shuffled_pass = ''.join(password)
print(f"The generated password is: %s" % shuffled_pass)
