MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

penny_value = 0.01
dime_value = 0.05
nickle_value = 0.10
quarters_value = 0.25

money = 0

is_on = True


def process(beverage, water, milk, coffee):

    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    total = (quarters * quarters_value) + (dimes * dime_value) + (nickles * nickle_value) + (pennies * penny_value)
    cost = MENU[beverage]["cost"]
    change = round(total - cost, 2)

    if change < 0:
        print("Sorry that's not enough money. Money refunded.")
    else:
        print(f"Here is ${change} in change.")
        global money
        global resources
        money += cost
        resources["water"] -= water
        resources["milk"] -= milk
        resources["coffee"] -= coffee
        print(f"Here is your {beverage}. Enjoy!")


def check_resources(beverage, water, milk, coffee):
    if resources["water"] < water:
        print("Sorry there is not enough water.")
    elif resources["milk"] < milk:
        print("Sorry there is not enough milk.")
    elif resources["coffee"] < coffee:
        print(f"Sorry there is not enough coffee.")
    else:
        process(beverage, water, milk, coffee)


while is_on:

    command = input("   What would you like? (espresso/latte/cappuccino): ").lower()

    if command == "off":
        is_on = False
    elif command == "report":
        print(f"Water : {resources['water']}ml")
        print(f"Milk  : {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money : ${money}")
    else:
        required_water = MENU[command]["ingredients"]["water"]
        required_milk = MENU[command]["ingredients"]["milk"]
        required_coffee = MENU[command]["ingredients"]["coffee"]
        check_resources(command, required_water, required_milk, required_coffee)
