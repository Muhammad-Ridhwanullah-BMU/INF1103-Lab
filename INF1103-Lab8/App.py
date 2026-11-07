from FileHandler import load_inventory, save_inventory
from DigitalProduct import DigitalProduct
from PhysicalProduct import PhysicalProduct
from CanBeShipped import CanBeShipped
from Inventory import Inventory

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

    print("1. Physical Product")
    print("2. Digital Product")
    product_type = input("Product Type (1 or 2): ").strip()
    if product_type not in ("1", "2"):
        print("Invalid product type. Please choose 1 or 2.")
        return

    product_id = input("Product ID: ").strip()
    if not product_id:
        print("Product ID cannot be empty.")
        return

    if inventory.find_product(product_id) is not None:
        print("Product ID already exists.")
        return

    product_name = input("Product Name: ").strip()
    if not product_name:
        print("Product name cannot be empty.")
        return

    try:
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))

    except ValueError:
        print("Price must be a non-negative number and stock a non-negative whole number.")
        return

    try:
        if int(product_type) == 1:
            weight = float(input("Weight: "))
            product = PhysicalProduct(product_id, product_name, price, stock, weight)
        else:
            download_size = float(input("Download Size: "))
            product = DigitalProduct(product_id, product_name, price, stock, download_size)

    except ValueError:
        if int(product_type) == 1:
            print("Weight must be a non-negative number")
        else:
            print("Download size must be a non-negative number")
        return

    if inventory.add_product(product):
        print("Product added to inventory successfully!")
    else:
        print("Product ID already exists.")

def update_stock(inventory):
    print("Update Stock")
    product_id = input("Enter Product ID: ").strip()
    product = inventory.find_product(product_id)

    if product is None:
        print("Product not found.")
        return

    print("Product Found:")
    product.display_information()

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
    product = inventory.find_product(product_id)

    if product is None:
        print("Product not found.")
        return

    print("Product Found")
    print("------------------------------------------------")
    product.display_information()
    print(product.get_fulfilment_info())
    if isinstance(product, CanBeShipped):
        print(f"Shipping cost: ${product.calculate_shipping_cost():.2f}")
    print("------------------------------------------------")

def remove_product(inventory):
    print("Search Product")
    product_id = input("Enter Product ID: ").strip()
    if inventory.remove_product(product_id):
        print("Product removed from inventory successfully!")
    else:
        print("There was en error removing the product from inventory.")   



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
