from turtle import clear
logo = """    __  ___  _____ _____  ___   ___      ___ ___  ____    __ __ __ ____ ____    ___     
   /  ]/   \|     |     |/  _] /  _]    |   |   |/    |  /  ]  |  |    |    \  /  _]    
  /  /|     |   __|   __/  [_ /  [_     | _   _ |  o  | /  /|  |  ||  ||  _  |/  [_     
 /  / |  O  |  |_ |  |_|    _]    _]    |  \_/  |     |/  / |  _  ||  ||  |  |    _]    
/   \_|     |   _]|   _]   [_|   [_     |   |   |  _  /   \_|  |  ||  ||  |  |   [_     
\     |     |  |  |  | |     |     |    |   |   |  |  \     |  |  ||  ||  |  |     |    
 \____|\___/|__|  |__| |_____|_____|    |___|___|__|__|\____|__|__|____|__|__|_____| """

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": float(1.5),
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": float(2.5),
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": float(3.0),
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": float(0),
}


# def coffee_type(user_pick):
#     global resources
#     global coffee_type
#     if user_pick == "espresso":
#         coffee_type = MENU["espresso"]
#     if user_pick == "latte":
#         coffee_type = MENU["latte"]
#     if user_pick == "cappuccino":
#         coffee_type = MENU["cappuccino"]
#     return coffee_type


# check resources
def check_resources(coffee_type):
    global stop_program
    if coffee_type["ingredients"]["milk"] > resources["milk"]:
        print("Sorry there is not enough milk.")
        return False
    if coffee_type["ingredients"]["water"] > resources["water"]:
        print("Sorry there is not enough water.")
        return False
    if coffee_type["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry there is not enough coffee.")
        return False
    else:
        return True


# process coins
def process_coins():
    print("Please insert coins")
    quarters = float(input("How many quarters? ")) * .25
    dimes = float(input("How many dimes? ")) * .10
    nickels = float(input("How many nickels? ")) * .05
    pennies = float(input("How many pennies? ")) * .01
    process_coins = float(quarters + dimes + nickels + pennies)
    return process_coins


# make coffee function
def make_coffee(coffee_type, user_pick):
    global resources
    resources["water"] -= int(coffee_type["ingredients"]["water"])
    resources["milk"] -= int(coffee_type["ingredients"]["milk"])
    resources["coffee"] -= int(coffee_type["ingredients"]["coffee"])
    print(f"Here is your {user_pick}. Enjoy!")


# check transaction successful
def check_transaction(processed_coins, coffee_type):
    if processed_coins < float(coffee_type["cost"]):
        print("Sorry that's not enough money. Money refunded")
        return False
    elif processed_coins >= float(coffee_type["cost"]):
        resources["money"] += coffee_type["cost"]
        change = processed_coins - coffee_type["cost"]
        if change != 0:
            print(f"Here is ${round(change, 2)} dollars in change.")
        return True


def coffee_machine():
    global MENU
    stop_program = True
    print(logo)

    while stop_program:

        user_pick = input("What would you like? (espresso/latte/cappuccino): ")

        if user_pick == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${resources['money']}")
        elif user_pick == 'off':
            clear()
            stop_program = False

        else:
            coffee_type = MENU[user_pick]
            if check_resources(coffee_type):
                processed_coins = process_coins()

                if check_transaction(processed_coins, coffee_type):
                    make_coffee(coffee_type, user_pick)


coffee_machine()







#




