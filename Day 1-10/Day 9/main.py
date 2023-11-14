# Calculator

# Import the required libraries

# Declare the required variables
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

print(logo)

# Add function -- add a list of numbers


def add(numbers):
    return sum(numbers)

# Subtract function -- subtract one number from another


def subtract(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

# Multiply function -- multiply a list of numbers


def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

# Division function -- divide a list of numbers


def division(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        if num == 0:
            print("Error! Cannot divide by zero.")
            return None
        result /= num
    return result

# Modulus function -- find remainder of a division operation


def modulo(numbers):
    if numbers[1] == 0:
        print("Error! Cannot divide by zero.")
        return None
    return numbers[0] % numbers[1]


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": division,
    "%": modulo
}

all_operations = []
previous_result = None

while True:
    num1 = int(input("What is the first number?: "))

    if previous_result is not None:
        print(f"Previous result: {previous_result}")

    numbers = [num1]

    while True:
        for symbol in operations:
            print(symbol)
        operation = input("Pick an operation from the line above: ")
        print("You picked:", operation)

        if operation not in operations:
            print("Invalid operator")
            break

        next_number = input("Enter the next number to calculate: ")

        if next_number.lower() == '=':
            break

        try:
            numbers.append(int(next_number))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

        result = operations[operation](numbers)
        print(f"The result so far is {result}")

        all_operations.append(f"{operation} {next_number} ")

        previous_result = result

        continue_calculation = input("Do you want to continue? (yes/no): ")
        if continue_calculation.lower() != 'yes':
            break

    end_program = input("Do you want to end the program? (yes/no): ")
    if end_program.lower() == 'yes':
        break

print(
    f"The final result of {num1} {' '.join(all_operations)} is = {result}")
