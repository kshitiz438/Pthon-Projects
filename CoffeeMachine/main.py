def calculation(coffee, paid, cost):
    """ Checks if the money paid in enough, if it's more, then calculates the refund """
    if paid < cost:
        return "Sorry that's not enough money. Money refunded"
    elif paid >= cost:
        refund = paid - cost
        return f"Here is ${refund} in change.\nHere is your {coffee}. Enjoy!!"


def coin_processing():
    """ Returns the amount paid by the user """
    print("Please insert the coins.")
    quarters = int(input("How many quarters? :"))
    dimes = int(input("How many dimes? :"))
    nickles = int(input("How many nickles? :"))
    pennies = int(input("How many pennies? :"))
    money_paid = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickles) + (0.01 * pennies)
    return money_paid


def is_enough_resources(order_ingredients):
    """  Checks if there are enough resources left  """
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
        else:
            return True


def ingredient_deduction(order_ingredients):
    """ Deducts the ingredients from the resources """
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]


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

profit = 0
resources = {
    "water": 3000,
    "milk": 2000,
    "coffee": 100,
}

next_order = True

while next_order:
    drink = input("What would you like? (espresso/latte/cappuccino): ")
    if drink == "espresso" or drink == "latte" or drink == "cappuccino":
        drink_chosen = MENU[drink]
        if is_enough_resources(drink_chosen["ingredients"]):
            ingredient_deduction(drink_chosen["ingredients"])
            paid_amount = coin_processing()
            drink_cost = MENU[drink]["cost"]
            print(calculation(drink, paid_amount, drink_cost))
            profit += drink_cost

    elif drink == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")

    elif drink == "off":
        next_order = False
