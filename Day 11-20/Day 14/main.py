# Coffee Machine

# 1. Import the required libraries/variables
from data import MENU, resources
import time
import os

# 2. Declare variables

logo = '''


 ██████╗ ██████╗ ███████╗███████╗███████╗███████╗    ████████╗ ██████╗        ██████╗  ██████╗ 
██╔════╝██╔═══██╗██╔════╝██╔════╝██╔════╝██╔════╝    ╚══██╔══╝██╔═══██╗      ██╔════╝ ██╔═══██╗
██║     ██║   ██║█████╗  █████╗  █████╗  █████╗         ██║   ██║   ██║█████╗██║  ███╗██║   ██║
██║     ██║   ██║██╔══╝  ██╔══╝  ██╔══╝  ██╔══╝         ██║   ██║   ██║╚════╝██║   ██║██║   ██║
╚██████╗╚██████╔╝██║     ██║     ███████╗███████╗       ██║   ╚██████╔╝      ╚██████╔╝╚██████╔╝
 ╚═════╝ ╚═════╝ ╚═╝     ╚═╝     ╚══════╝╚══════╝       ╚═╝    ╚═════╝        ╚═════╝  ╚═════╝ 
                                                                                               

'''

machine_on = True
PROFIT = 0


def check_order(order):
    missing_ingredients = []

    for item in order:
        if order[item] > resources[item]:
            missing_ingredients.append(item)

    if missing_ingredients:
        print("Sorry, you are missing the following ingredients:")
        for ingredient in missing_ingredients:
            if ingredient in ['water', 'milk']:
                print(
                    f"- {ingredient}: {abs(resources[ingredient] - order[ingredient])} ml")
            elif ingredient == 'coffee':
                print(
                    f"- {ingredient}: {abs(resources[ingredient] - order[ingredient])} gms")
        return False
    else:
        return True


def process_order():
    print("Please insert coins....")
    total = 0
    print("**********************")
    total += int(input("How many quarters?:")) * 0.25
    total += int(input("How many dimes?:")) * 0.10
    total += int(input("How many nickels?:"))*0.05
    total += int(input("How many pennies?:"))*0.01
    print("**********************")
    return total


def check_transaction(money, cost):
    if money >= cost:
        change = round(money - cost, 2)
        print(
            f"The cost of your drink is {cost:.2f}$ and you have inserted {money:.2f}$")
        print(f"Your change will be {change}$")
        global PROFIT
        PROFIT += cost
        return True
    else:
        print("Sorry, there is not enough money to make this transaction. MONEY REFUNDED")
        return False


def make_coffee(drink, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Making {drink}...")


def add_extra_ingredients():
    print("Add extra ingredients:")
    extra_water = int(input("How much extra water (in ml)?: "))
    extra_milk = int(input("How much extra milk (in ml)?: "))
    extra_coffee = int(input("How much extra coffee (in gms)?: "))

    # Update the resources dictionary with the extra ingredients
    resources['water'] += extra_water
    resources['milk'] += extra_milk
    resources['coffee'] += extra_coffee

    print("Extra ingredients added successfully.")


print(logo)

while machine_on:
    choice = input(
        "Which kind of coffee do you want to order (espresso/latte/cappuccino)?:")
    if choice == 'off':
        print("Turning off the machine...")
        machine_on = False
    elif choice == 'report':
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} gms")
        print(f"Money: {PROFIT:.2f}$")
    elif choice == 'add':
        add_extra_ingredients()
    else:
        drink = MENU[choice]
        if check_order(drink['ingredients']):
            print('Preparing your order')
            payment = process_order()
            if check_transaction(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])
