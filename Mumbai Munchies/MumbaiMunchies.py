import json

def allSnacks():
    file_path = "snacks.json"

    try:
        with open(file_path, "r") as json_file:
            snacks_data = json.load(json_file)
    except FileNotFoundError:
        snacks_data = []

    for snack in snacks_data:
        name = snack["name"]
        price = snack["price"]
        availability = "yes" if snack["availability"] else "no"

        print(f"name {name}  price = ${price} Availability = {availability}")




import json

def addNewSnack():
    file_path = "snacks.json"
    try:
        with open(file_path, "r") as json_file:
            snacks_data = json.load(json_file)
    except FileNotFoundError:
        snacks_data = []

    while True:
        
        name = input("Enter snack name (or type 'exit' to stop adding): ")
        if name.lower() == "exit":
            break

        price = float(input("Enter snack price: "))
        availability = input("Is the snack available (yes/no): ").lower() == "yes"

        new_snack = {
            "name": name,
            "price": price,
            "availability": availability
        }

        snacks_data.append(new_snack)

    with open(file_path, "w") as json_file:
        json.dump(snacks_data, json_file, indent=4)




def removeSnacks():
    file_path = "snacks.json"
    try:
        with open(file_path, "r") as json_file:
            snacks_data = json.load(json_file)
    except FileNotFoundError:
        snacks_data = []

    name_to_remove = input("Enter the name of the snack to remove: ")
    removed_snacks = [snack for snack in snacks_data if snack["name"] != name_to_remove]

    if len(removed_snacks) == len(snacks_data):
        print(f"No snack with the name '{name_to_remove}' found.")
        return
    with open(file_path, "w") as json_file:
        json.dump(removed_snacks, json_file, indent=4)

    print(f"Snack '{name_to_remove}' has been removed.")




def updateAvailability():
    file_path = "snacks.json"
    try:
        with open(file_path, "r") as json_file:
            snacks_data = json.load(json_file)
    except FileNotFoundError:
        snacks_data = []

    name_to_update = input("Enter the name of the snack to update availability: ")

    
    snack_updated = False
    for snack in snacks_data:
        if snack["name"] == name_to_update:
            snack["availability"] = not snack["availability"]
            snack_updated = True
            break

    if not snack_updated:
        print(f"No snack with the name '{name_to_update}' found.")
        return

    with open(file_path, "w") as json_file:
        json.dump(snacks_data, json_file, indent=4)

    print(f"Availability of snack '{name_to_update}' has been updated.")




def buySnack():
    file_path = "snacks.json"

    try:
        with open(file_path, "r") as json_file:
            snacks_data = json.load(json_file)
    except FileNotFoundError:
        snacks_data = []

    name_to_buy = input("Enter the name of the snack you want to buy: ")

    snack_found = False
    for snack in snacks_data:
        if snack["name"] == name_to_buy:
            if snack["availability"]:
                print(f"You have bought '{name_to_buy}'. Enjoy!")
                snack["availability"] = False
            else:
                print(f"'{name_to_buy}' is currently not available.")
            snack_found = True
            break

    if not snack_found:
        print(f"No snack with the name '{name_to_buy}' found.")

    with open(file_path, "w") as json_file:
        json.dump(snacks_data, json_file, indent=4)





def main():
 while True:
    print("Welcome to Mumbai Munches\n===========================")
    print("1.View All The Snacks\n2.Add a New Snack\n3.Remove Snack\n4.Update Snack Availability\n5.Buy a Snack\n6.Exit\n===========================")
    opt=int(input("Choose Option(1-6)\n"))
    if opt==1:
      print("\n==========All Snacks===========")
      allSnacks()
    elif opt==2:
       print("\n==========Add Snacks===========")
       addNewSnack()
    elif opt==3:
       print("\n==========Remove Snacks========")
       removeSnacks()
    elif opt==4:
       print("\n==========Update Snacks========")
       updateAvailability()
    elif opt==5:
       print("\n==========Buy Snack===========")
       buySnack()
    elif opt==6:
       print("Thank You For The Visit")
       break


main()