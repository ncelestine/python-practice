MENU = {
    "espresso": {"water": 50, "milk": 0, "coffee": 18, "cost": 1.5},
    "latte": {"water": 200, "milk": 150, "coffee": 24, "cost": 2.5},
    "cappuccino": {"water": 250, "milk": 100, "coffee": 24, "cost": 3.0}
}

resources = {"water": 300, "milk": 200, "coffee": 100, "money": 0}


def print_report():
    #Prints the current resources report.
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']:.2f}")


def check_resources(drink):
    #Returns True if resources are sufficient, False otherwise.
    for item in MENU[drink]:
        if item != "cost" and MENU[drink][item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    #This processes the coin input from the user and returns the total amount.
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickels = int(input("How many nickels?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    return round(quarters + dimes + nickels + pennies, 2)


def transaction_successful(money_received, drink):
    """Checks if payment is sufficient and returns True if successful, False otherwise."""
    cost = MENU[drink]["cost"]
    if money_received < cost:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    else:
        change = round(money_received - cost, 2)
        if change > 0:
            print(f"Here is ${change} in change.")
        resources["money"] += cost
        return True


def make_coffee(drink):
    """Deducts the required resources and serves the coffee."""
    for item in MENU[drink]:
        if item != "cost":
            resources[item] -= MENU[drink][item]
    print(f"Here is your {drink}. Enjoy!")


def coffee_machine():
    """Main function to run the coffee machine."""
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice == "off":
            print("Turning off the coffee machine.")
            break
        elif choice == "report":
            print_report()
        elif choice in MENU:
            if check_resources(choice):
                print(f"The price of {choice} is ${MENU[choice]['cost']:.2f}. Please insert coins.")
                payment = process_coins()
                if transaction_successful(payment, choice):
                    make_coffee(choice)
        else:
            print("Invalid choice. Please select a valid option.")


# Run the coffee machine
coffee_machine()
