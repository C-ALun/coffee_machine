from data import resources, MENU

#TODO-1 check is resource sufficient
def is_resource_sufficient(machine_details, order_ingredients):
    for item in machine_details:
        if machine_details[item] < order_ingredients[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        return True


#TODO-2 make a function to process coins
def process_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


#TODO-3 check is the transaction successful
def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


#TODO-4 A function to produce coffee
def make_coffee(drink_name, order_ingredients, machine_details):
    for item in machine_details:
        machine_details[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

is_off = False
machine_details = resources
profit = 0

while not is_off:

    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == 'off':
        is_off = True
    elif choice == 'report':
        print(f"Water: {machine_details['water']}ml")
        print(f"Milk: {machine_details['milk']}ml")
        print(f"Coffee: {machine_details['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(machine_details, drink['ingredients']):
            cost = process_coins()
            if is_transaction_successful(cost, drink['cost']):
                make_coffee(choice, drink['ingredients'], machine_details)