import json
import os
from Inventory import Inventory
from Product import Product

FILE_NAME = "inventory.json"
FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), FILE_NAME)

def load_inventory():

    inventory = Inventory()

    if not os.path.exists(FILE_PATH):
        print("Starting with empty inventory.")
        return inventory

    try:
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            saved_products = json.load(file)

        if not isinstance(saved_products, list):
            raise ValueError("Inventory must contain a list of products.")

    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as error:
        print(f"Unable to load {FILE_NAME}: {error}")
        print("Starting with empty inventory.")
        return inventory

    for data in saved_products:
        try:
            if not isinstance(data, dict):
                raise ValueError("Product record must be a dictionary.")

            product = Product(
                data["id"],
                data["name"],
                data["price"],
                data["stock"],
            )

            if not inventory.add_product(product):
                print(f"Skipped duplicate product ID: {product.get_product_id()}")
        except (KeyError, TypeError, ValueError, AttributeError):
            print("Skipped an invalid product in the inventory file.")
    return inventory

def save_inventory(inventory, exit_save=False):
    #Write the data of all Product instances to a list in inventory.json
    products = [product.to_dictionary() for product in inventory.get_products()]

    try:
        with open(FILE_PATH, "w", encoding="utf-8") as file:
            json.dump(products, file, indent=4, allow_nan=False)
    except (OSError, UnicodeError, TypeError, ValueError) as error:
        print(f"Unable to save {FILE_NAME}: {error}")
        return False

    if exit_save:
        print("Inventory saved successfully.")
    else:
        print(f"Inventory saved successfully to {FILE_NAME}.")
    return True

