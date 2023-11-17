from menu import MenuItem, Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

logo = '''


 ██████╗ ██████╗ ███████╗███████╗███████╗███████╗    ████████╗ ██████╗        ██████╗  ██████╗ 
██╔════╝██╔═══██╗██╔════╝██╔════╝██╔════╝██╔════╝    ╚══██╔══╝██╔═══██╗      ██╔════╝ ██╔═══██╗
██║     ██║   ██║█████╗  █████╗  █████╗  █████╗         ██║   ██║   ██║█████╗██║  ███╗██║   ██║
██║     ██║   ██║██╔══╝  ██╔══╝  ██╔══╝  ██╔══╝         ██║   ██║   ██║╚════╝██║   ██║██║   ██║
╚██████╗╚██████╔╝██║     ██║     ███████╗███████╗       ██║   ╚██████╔╝      ╚██████╔╝╚██████╔╝
 ╚═════╝ ╚═════╝ ╚═╝     ╚═╝     ╚══════╝╚══════╝       ╚═╝    ╚═════╝        ╚═════╝  ╚═════╝ 
                                                                                               

'''

print(logo)

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

machine_on = True

while machine_on:
    options = menu.get_items()
    user_choice = input(
        f"Which kind of coffee do you want to order ({options})?: ")
    if user_choice == "off":
        print("Turning machine off...")
        machine_on = False
    elif user_choice == 'report':
        coffee_maker.report()
        money_machine.report()
    elif user_choice == 'add':
        coffee_maker.add_extra_ingredients()
    else:
        drink = menu.find_drink(user_choice)
        if (coffee_maker.check_order(drink)) and (money_machine.process_order(drink.cost)):
            print("Preparing your order....")
            if money_machine.check_transaction(drink.cost):
                coffee_maker.make_coffee(drink)
