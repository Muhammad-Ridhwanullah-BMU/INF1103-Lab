import json
import os

FILE_NAME = "inventory.json"
FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), FILE_NAME)

inventory = []


def load_inventory():
    global inventory

    if os.path.exists(FILE_PATH):
        print(f"{FILE_NAME} found.")

        try:
            with open(FILE_PATH, "r", encoding="utf-8") as file:
                inventory = json.load(file)

            print("Inventory loaded successfully.")

        except (json.JSONDecodeError, TypeError):
            print("Inventory file contains invalid JSON. Starting with empty inventory.")
            inventory = []

    else:
        print(f"{FILE_NAME} not found.")
        print("Starting with empty inventory.")
        inventory = []


def save_inventory(exit_save=False):
    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(inventory, file, indent=4)

    if exit_save:
        print("Inventory saved successfully.")
    else:
        print(f"Inventory saved successfully to {FILE_NAME}.")


def display_all():
    print("Current Inventory")
    print("------------------------------------------------")

    if len(inventory) == 0:
        print("No products in inventory.")
    else:
        for product in inventory:
            print(
                f"ID: {product['id']} | "
                f"Name: {product['name']} | "
                f"Price: ${product['price']:.2f} | "
                f"Stock: {product['stock']}"
            )

    print("------------------------------------------------")


def add_product():
    print("Add New Product")

    product_id = input("Product ID: ").strip()

    for product in inventory:
        if product["id"].lower() == product_id.lower():
            print("Product ID already exists.")
            return

    product_name = input("Product Name: ").strip()

    try:
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))

        if price < 0 or stock < 0:
            print("Price and stock cannot be negative.")
            return

    except ValueError:
        print("Price must be a number and stock must be a whole number.")
        return

    product = {
        "id": product_id,
        "name": product_name,
        "price": price,
        "stock": stock
    }

    inventory.append(product)
    print("Product added successfully!")


def update_stock():
    print("Update Stock")
    product_id = input("Enter Product ID: ").strip()

    for product in inventory:
        if product["id"].lower() == product_id.lower():
            print("Product Found:")
            print(f"Name: {product['name']}")
            print(f"Current Stock: {product['stock']}")

            try:
                new_stock = int(input("New Stock Quantity: "))

                if new_stock < 0:
                    print("Stock cannot be negative.")
                    return

            except ValueError:
                print("Stock must be a whole number.")
                return

            product["stock"] = new_stock
            print("Stock updated successfully!")
            return

    print("Product not found.")


def search_product():
    print("Search Product")
    product_id = input("Enter Product ID: ").strip()

    for product in inventory:
        if product["id"].lower() == product_id.lower():
            print("Product Found")
            print("------------------------------------------------")
            print(f"ID: {product['id']}")
            print(f"Name: {product['name']}")
            print(f"Price: ${product['price']:.2f}")
            print(f"Stock: {product['stock']}")
            print("------------------------------------------------")
            return

    print("Product not found.")


def main_menu():
    print("----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")

def main():
    print("========================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("========================================")

    load_inventory()
    main_menu()

    while True:
        option = input("Enter option: ").strip()

        if option == "1":
            display_all()

        elif option == "2":
            add_product()

        elif option == "3":
            update_stock()

        elif option == "4":
            search_product()

        elif option == "5":
            print("Saving inventory...")
            save_inventory()

        elif option == "6":
            print("Saving inventory before exit...")
            save_inventory(exit_save=True)
            print("Thank you for using Inventory Management System.")
            print("Program terminated.")
            break

        else:
            print("Invalid option. Please enter a number from 1 to 6.")

        print()

if __name__ == "__main__":
    main()
