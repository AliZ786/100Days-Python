class MoneyMachine:
    CURRENCY = "$"

    COIN_VALUES = {
        "Penny": 0.01,
        "Nickel": 0.05,
        "Dime": 0.10,
        "Quarter": 0.25,
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        print(f"Money: {self.profit:.2f}{self.CURRENCY}")

    def process_order(self, drink):
        print("Please insert coins....")
        self.money_received = 0
        print("**********************")
        self.money_received += int(input("How many quarters?:")) * \
            self.COIN_VALUES["Quarter"]
        self.money_received += int(input("How many dimes?:")
                                   ) * self.COIN_VALUES["Dime"]
        self.money_received += int(input("How many nickels?:")
                                   ) * self.COIN_VALUES["Nickel"]
        self.money_received += int(input("How many pennies?:")
                                   )*self.COIN_VALUES["Penny"]
        print("**********************")
        return self.money_received

    def check_transaction(self, cost):
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(
                f"The cost of your drink is {cost:.2f}$ and you have inserted {self.money_received:.2f}{self.CURRENCY}")
            print(f"Your change will be {change}$")
            self.profit += cost
            return True
        else:
            print(
                "Sorry, there is not enough money to make this transaction. MONEY REFUNDED")
            return False
