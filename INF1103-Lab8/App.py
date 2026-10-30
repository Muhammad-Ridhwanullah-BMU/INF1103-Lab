from FileHandler import load_inventory, save_inventory
from Product import Product

def main_menu():
    print("----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")

def add_product(inventory):
    print("Add New Product")

    product_id = input("Product ID: ").strip()
    if not product_id:
        print("Product ID cannot be empty.")
        return

    if inventory.search_product(product_id) is not None:
        print("Product ID already exists.")
        return

    product_name = input("Product Name: ").strip()
    if not product_name:
        print("Product name cannot be empty.")
        return

    try:
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))
        product = Product(product_id, product_name, price, stock)
    except ValueError:
        print("Price must be a non-negative number and stock a non-negative whole number.")
        return

    if inventory.add_product(product):
        print("Product added successfully!")
    else:
        print("Product ID already exists.")

def update_stock(inventory):
    print("Update Stock")
    product_id = input("Enter Product ID: ").strip()
    product = inventory.search_product(product_id)

    if product is None:
        print("Product not found.")
        return

    print("Product Found:")
    print("------------------------------------------------")
    print(f"ID: {product.get_product_id()} | "
          f"Name: {product.get_name()} | "
          f"Current Stock: {product.get_stock()}")
    print("------------------------------------------------")

    try:
        new_stock = int(input("New Stock Quantity: "))
        product.update_stock(new_stock)
    except ValueError:
        print("Stock must be a non-negative whole number.")
        return

    print("Stock updated successfully!")

def search_product(inventory):
    print("Search Product")
    product_id = input("Enter Product ID: ").strip()
    product = inventory.search_product(product_id)

    if product is None:
        print("Product not found.")
        return

    print("Product Found")
    print("------------------------------------------------")
    product.display_information()
    print("------------------------------------------------")

def main():
    print("========================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("========================================")

    # FileHandler reconstructs Inventory and Product objects from JSON.
    inventory = load_inventory()

    while True:
        main_menu()
        try:
            option = input("Enter option: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nSaving inventory before exit...")
            save_inventory(inventory, exit_save=True)
            print("Program terminated.")
            break

        if option == "1":
            inventory.display_all()
        elif option == "2":
            add_product(inventory)
        elif option == "3":
            update_stock(inventory)
        elif option == "4":
            search_product(inventory)
        elif option == "5":
            print("Saving inventory...")
            save_inventory(inventory)
        elif option == "6":
            print("Saving inventory before exit...")
            save_inventory(inventory, exit_save=True)
            print("==========================================================")
            print("Thank you for using Inventory Management System.")
            print("Program terminated.")
            print("==========================================================")
            break
        else:
            print("Invalid option. Please enter a number from 1 to 6.")

        print()


if __name__ == "__main__":
    main()
