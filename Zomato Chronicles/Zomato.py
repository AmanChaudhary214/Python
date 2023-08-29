import json

def displayMenu():
    file_path = "menu.json"

    try:
        with open(file_path, "r") as json_file:
            snacks_data = json.load(json_file)
    except FileNotFoundError:
        snacks_data = []

    
    for snack in snacks_data:
        name = snack["dish_name"]
        price = snack["price"]
        availability = "yes" if snack["availability"] else "no"

        print(f"name {name}  price = ${price} Availability = {availability}")




import json

def addNewSnack():
    file_path = "menu.json"
    try:
        with open(file_path, "r") as json_file:
            snacks_data = json.load(json_file)
    except FileNotFoundError:
        snacks_data = []

    while True:
        
        name = input("Enter Dish name (or type 'exit' to stop adding): ")
        if name.lower() == "exit":
            break

        price = float(input("Enter Dish price: "))
        availability = input("Is the DISH available (yes/no): ").lower() == "yes"

        
        new_snack = {
            "dish_name": name,
            "price": price,
            "availability": availability
        }

        
        snacks_data.append(new_snack)

    
    with open(file_path, "w") as json_file:
        json.dump(snacks_data, json_file, indent=4)



 


def  remove_dish_by_name():
    file_path = "menu.json"
    try:
        with open(file_path, "r") as json_file:
            snacks_data = json.load(json_file)
    except FileNotFoundError:
        snacks_data = []

    name_to_remove = input("Enter the name of the dish to remove: ")
    removed_snacks = [snack for snack in snacks_data if snack["dish_name"] != name_to_remove]

    if len(removed_snacks) == len(snacks_data):
        print(f"No snack with the name '{name_to_remove}' found.")
        return
    with open(file_path, "w") as json_file:
        json.dump(removed_snacks, json_file, indent=4)

    print(f"dish '{name_to_remove}' has been removed.")





def updateAvailability():
    file_path = "menu.json"
    try:
        with open(file_path, "r") as json_file:
            snacks_data = json.load(json_file)
    except FileNotFoundError:
        snacks_data = []

    name_to_update = input("Enter the name of the dish to update availability: ")

    
    snack_updated = False
    for snack in snacks_data:
        if snack["dish_name"] == name_to_update:
            snack["availability"] = not snack["availability"]
            snack_updated = True
            break

    if not snack_updated:
        print(f"No dish with the name '{name_to_update}' found.")
        return

    with open(file_path, "w") as json_file:
        json.dump(snacks_data, json_file, indent=4)

    print(f"Availability of dish '{name_to_update}' has been updated.")






def buySnack():
    file_path = "menu.json"

    try:
        with open(file_path, "r") as json_file:
            snacks_data = json.load(json_file)
    except FileNotFoundError:
        snacks_data = []

    name_to_buy = input("Enter the name of the dish you want to buy: ")

    snack_found = False
    for snack in snacks_data:
        if snack["dish_name"] == name_to_buy:
            if snack["availability"]:
                print(f"You have bought '{name_to_buy}'. Enjoy!")
                snack["availability"] = False
            else:
                print(f"'{name_to_buy}' is currently not available.")
            snack_found = True
            break

    if not snack_found:
        print(f"No dish with the name '{name_to_buy}' found.")

    with open(file_path, "w") as json_file:
        json.dump(snacks_data, json_file, indent=4)










def main():
    while True:
        print("Welcome to Zesty Zomato!")
        print("0. Display Menu")
        print("1. Add Dish")
        print("2. Remove Dish")
        print("3. Update Dish Availability")
        print("4. Take Order")
        print("5. Update Order Status")
        print("6. Review Orders")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '0':
            print("\nMENU")
            displayMenu()
        elif choice == '1':
            addNewSnack
            # Implement adding a new dish
            pass
        elif choice == '2':
            print("/nREMOVE DISH")
            remove_dish_by_name()
            pass
        elif choice == '3':
            updateAvailability()
            # Implement updating dish availability
            pass
        elif choice == '4':
            # Implement taking a new order
            pass
        elif choice == '5':
            # Implement updating order status
            pass
        elif choice == '6':
            # Implement reviewing orders
            pass
        elif choice == '7':
            print("Thank you for using Zesty Zomato!")
            break
        else:
            print("Invalid choice. Please select a valid option.")




main()
