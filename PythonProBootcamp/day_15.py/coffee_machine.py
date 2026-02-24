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
    "money": 0,
}
coins = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickels": 0.05,
    "pennies": 0.01,
}

while True:
    input_ = input("What would you like? (espresso/latte/cappuccino): ")
    if input_ in MENU:
        resource_check = True
        for ingredient in MENU[input_]["ingredients"]:
            if resources[ingredient] < MENU[input_]["ingredients"][ingredient]:
                print(f"Sorry there is not enough {ingredient}.")
                break
            else:
                resource_check = False
        if resource_check:
            break
    if input_ == "off": 
        break
    elif input_ == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")
    elif input_ in MENU:
        if resources["money"] < MENU[input_]["cost"]:
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickels = int(input("How many nickels?: "))
            pennies = int(input("How many pennies?: "))
            resources["money"] += quarters * coins["quarters"] + dimes * coins["dimes"] + nickels * coins["nickels"] + pennies * coins["pennies"]
        total = resources["money"]
        if total < MENU[input_]["cost"]:
            print("Sorry that's not enough money. Money refunded.")
        else:               
            change = round(total - MENU[input_]["cost"], 2)
            resources["money"] -= MENU[input_]["cost"]
            for ingredient in MENU[input_]["ingredients"]:
                resources[ingredient] -= MENU[input_]["ingredients"][ingredient]     
            print(f"Here is ${change} in change.")
            print(f"Here is your {input_}. Enjoy!")