import json

data_file = "data.json"

def load_data():
    try:
        with open(data_file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []



def save_data(items):
    with open(data_file, "w") as f:
        json.dump(items, f, indent=4)

        

def add_item():
    items = load_data()

    item_id = input("Enter Item ID: ")
    item_name = input("Enter Item Name: ")
    price = float(input("Enter Price: "))
    availability = input("Is the item available (yes/no): ").lower()

    new_item = {
        "item_id": item_id,
        "item_name": item_name,
        "price": price,
        "availability": availability == "yes"
    }

    items.append(new_item)
    save_data(items)
    print("Item added successfully!")



def update_item():
    items = load_data()

    item_id = input("Enter Item ID of the item to update: ")

    found_item = None
    for item in items:
        if item["item_id"] == item_id:
            found_item = item
            break

    if found_item is None:
        print("Item not found.")
        return

    print("Found Item:")
    print(f"Item ID: {found_item['item_id']}")
    print(f"Item Name: {found_item['item_name']}")
    print(f"Price: {found_item['price']}")
    print(f"Availability: {'Available' if found_item['availability'] else 'Not Available'}")
    print("-" * 30)

    choice = input("Do you want to update this item? (yes/no): ").lower()
    if choice == "yes":
        found_item["item_name"] = input("Enter new Item Name: ")
        found_item["price"] = float(input("Enter new Price: "))
        new_availability = input("Is the item available (yes/no): ").lower()
        found_item["availability"] = new_availability == "yes"
        save_data(items)
        print("Item updated successfully!")



def view_inventory():
    items = load_data()

    if not items:
        print("No items available.")
        return

    print("List of Items:")
    for item in items:
        availability = "Available" if item["availability"] else "Not Available"
        print(f"Item ID: {item['item_id']}")
        print(f"Item Name: {item['item_name']}")
        print(f"Price: {item['price']}")
        print(f"Availability: {availability}")
        print("-" * 30)



def remove_item() :
    items = load_data()

    item_id = input("Enter Item ID of the item to delete: ")

    found_item = None
    for item in items:
        if item["item_id"] == item_id:
            found_item = item
            break

    if found_item is None:
        print("Item not found.")
        return

    print("Found Item:")
    print(f"Item ID: {found_item['item_id']}")
    print(f"Item Name: {found_item['item_name']}")
    print(f"Price: {found_item['price']}")
    print(f"Availability: {'Available' if found_item['availability'] else 'Not Available'}")
    print("-" * 30)

    choice = input("Do you want to delete this item? (yes/no): ").lower()
    if choice == "yes":
        items.remove(found_item)
        save_data(items)
        print("Item deleted successfully!")
    


def place_order() :
    items = load_data()

    print("List of Available Items:")
    available_items = [item for item in items if item["availability"]]
    if not available_items:
        print("No items available for sale.")
        return

    print("Available Items:")
    for item in available_items:
        print(f"Item ID: {item['item_id']}")
        print(f"Item Name: {item['item_name']}")
        print(f"Price: {item['price']}")
        print("-" * 30)

    item_id = input("Enter Item ID of the item to sell: ")

    found_item = None
    for item in available_items:
        if item["item_id"] == item_id:
            found_item = item
            break

    if found_item is None:
        print("Item not found.")
        return

    print("Found Item:")
    print(f"Item ID: {found_item['item_id']}")
    print(f"Item Name: {found_item['item_name']}")
    print(f"Price: {found_item['price']}")
    print("-" * 30)

    quantity = int(input("Enter the quantity to sell: "))

    total_price = found_item["price"] * quantity
    print(f"Total Price: {total_price}")

    choice = input("Confirm sale? (yes/no): ").lower()
    if choice == "yes":
        found_item["availability"] = False
        save_data(items)
        record_sale(found_item["item_name"], quantity, total_price)
        print("Sale recorded successfully!")



def record_sale(item_name, quantity, total_price):
    with open("sales_records.txt", "a") as f:
        f.write(f"Item: {item_name}\n")
        f.write(f"Quantity: {quantity}\n")
        f.write(f"Total Price: {total_price}\n")
        f.write("-" * 30 + "\n")  

    

def display() :
    print("")
    print("      WELCOME TO MUMBAI MUNCHIES      ")
    print("======================================")
    print("          Services Available          ")
    print("--------------------------------------")
    print("1 - Add item")
    print("2 - Update item")
    print("3 - Remove item")
    print("4 - View Inventory")
    print("5 - Place order")
    print("6 - Sales Record")
    print("0 - Exit")
    print("======================================")



def menu(choice) :
    if choice == 1:
        add_item()
    elif choice == 2:
        update_item()
    elif choice == 3:
        remove_item()
    elif choice == 4:
        view_inventory()
    elif choice == 5:
        place_order()
    else:
        record_sale()



def main():
    while True :
        display()
        choice = int(input("Enter 0-6 to perform desired operation: "))
        if choice in range(1,7):
            menu(choice)
        elif choice == 0 :
            print("Thank you for visiting Mumbai Munchies")
            break
        else:
            print("Invalid choice. Please choose again.")

        print(f"You chose: {choice}")
        
    

if __name__ == "__main__":
    main()
