class CoffeeMaker:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        print(f"Water: {self.resources['water']} ml")
        print(f"Milk: {self.resources['milk']} ml")
        print(f"Coffee: {self.resources['coffee']} gms")

    def check_order(self, order):
        missing_ingredients = []

        for ingredient, quantity in order.ingredients.items():
            if quantity > self.resources[ingredient]:
                missing_ingredients.append(ingredient)

        if missing_ingredients:
            print("Sorry, you are missing the following ingredients:")
            for ingredient in missing_ingredients:
                if ingredient in ['water', 'milk']:
                    print(
                        f"- {ingredient}: {abs(self.resources[ingredient] - order.ingredients[ingredient])} ml")
                elif ingredient == 'coffee':
                    print(
                        f"- {ingredient}: {abs(self.resources[ingredient] - order.ingredients[ingredient])} gms")
            return False
        else:
            return True

    def make_coffee(self, drink):
        if self.check_order(drink):
            for ingredient, quantity in drink.ingredients.items():
                self.resources[ingredient] -= quantity
        print(f"Making {drink.name}...")

    def add_extra_ingredients(self):
        print("Add extra ingredients:")
        extra_water = int(input("How much extra water (in ml)?: "))
        extra_milk = int(input("How much extra milk (in ml)?: "))
        extra_coffee = int(input("How much extra coffee (in gms)?: "))

        # Update the resources dictionary with the extra ingredients
        self.resources['water'] += extra_water
        self.resources['milk'] += extra_milk
        self.resources['coffee'] += extra_coffee

        print("Extra ingredients added successfully.")
