
import os

# File to store menu data
MENU_FILE = "menu.txt"

def load_menu():
    """Loads the menu from the text file."""
    if not os.path.exists(MENU_FILE):
        return {}
    with open(MENU_FILE, "r") as file:
        lines = file.readlines()
        menu = {}
        for line in lines:
            item, price = line.strip().split(" - $")
            menu[item] = float(price)
        return menu

def save_menu(menu):
    """Saves the menu to the text file."""
    with open(MENU_FILE, "w") as file:
        for item, price in menu.items():
            file.write(f"{item} - ${price:.2f}\n")

def display_menu(menu):
    """Displays the menu."""
    if not menu:
        print("\nThe menu is empty.\n")
    else:
        print("\nCurrent Menu:")
        for item, price in menu.items():
            print(f"{item}: ${price:.2f}")
        print()

def add_item(menu):
    """Adds a new item to the menu."""
    item = input("Enter the name of the item: ").strip()
    if item in menu:
        print("Item already exists in the menu.\n")
        return
    try:
        price = float(input(f"Enter the price for {item}: "))
        menu[item] = price
        print(f"{item} has been added to the menu.\n")
    except ValueError:
        print("Invalid price. Please try again.\n")

def remove_item(menu):
    """Removes an item from the menu."""
    item = input("Enter the name of the item to remove: ").strip()
    if item in menu:
        del menu[item]
        print(f"{item} has been removed from the menu.\n")
    else:
        print("Item not found in the menu.\n")

def edit_item(menu):
    """Edits an existing item in the menu."""
    item = input("Enter the name of the item to edit: ").strip()
    if item in menu:
        try:
            new_price = float(input(f"Enter the new price for {item}: "))
            menu[item] = new_price
            print(f"The price of {item} has been updated to ${new_price:.2f}.\n")
        except ValueError:
            print("Invalid price. Please try again.\n")
    else:
        print("Item not found in the menu.\n")

def main():
    """Main program loop."""
    menu = load_menu()

    while True:
        print("Restaurant Menu Options:")
        print("1. Display Menu")
        print("2. Add Item")
        print("3. Remove Item")
        print("4. Edit Item")
        print("5. Exit")
        
        choice = input("Choose an option: ").strip()
        if choice == "1":
            display_menu(menu)
        elif choice == "2":
            add_item(menu)
        elif choice == "3":
            remove_item(menu)
        elif choice == "4":
            edit_item(menu)
        elif choice == "5":
            save_menu(menu)
            print("Menu saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
