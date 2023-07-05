# day15 Project - Coffee Machine

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# Print report
def report():
    print(f"Water: {resources['water']}ml \n"
          f"Milk: {resources['milk']}ml \n"
          f"Coffee: {resources['coffee']}g\n"
          f"Money: ${money_box}\n")


# Check resources
def check_resources(ingredients):
    """Returns True when sufficient ingredients are available, False if insufficient"""
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print(f"Not enough {item}")
            return False
    return True


# Process Coins
def process_coins():
    """Returns total calculated from coins inserted"""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


# Check Transaction
def is_transaction_successful(money_received, drink_cost):
    """Return True when payment is accepted, False if money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global money_box
        money_box += drink_cost
        return True

    else:
        print("Sorry, that's not enough money, here is your refund.\n\n")
        return False


# Make Coffee
def make_coffee(drink_name, ingredients):
    """Deduct required ingredients from resources/"""
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink_name}, enjoy!\n\n")


# Coffee Machine
money_box = 0
is_on = True

while is_on:
    choice = input("What would you like? \nEspresso, Latte, Cappuccino: \n").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        report()
    else:
        drink = MENU[choice]
        if check_resources(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])