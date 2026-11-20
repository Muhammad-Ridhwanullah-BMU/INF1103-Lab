import json
import os
from Inventory import Inventory
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from Supplier import Supplier
from ProductFactory import ProductFactory

FILE_NAME = "inventory.json"
FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), FILE_NAME)

def load_inventory() -> Inventory:

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

    suppliers: dict[str, Supplier] = {}

    for index, data in enumerate(saved_products, start=1):
        try:
            if not isinstance(data, dict):
                raise ValueError("Product record must be a dictionary.")

            supplier_data = data["supplier"]

            if not isinstance(supplier_data, dict):
                raise ValueError("supplier must be a dictionary.")

            supplier_id = supplier_data["supplier_id"]

            if not isinstance(supplier_id, str):
                raise ValueError("Supplier ID must be text.")

            key = supplier_id.strip().casefold()
            supplier = suppliers.get(key)

            if supplier is None:
                supplier = Supplier(
                    supplier_data["supplier_id"],
                    supplier_data["name"],
                    supplier_data["contact_email"]
                )
                suppliers[key] = supplier

            elif supplier.to_dictionary() != supplier_data:
                raise ValueError("Supplier ID has conflicting details.")

            # Determine product type
            product_type = data.get("type")

            if product_type is None:
                if "weight" in data and "download_size" in data:
                    raise ValueError(
                        "Both weight and download_size are present."
                    )

                if "weight" in data:
                    product_type = "physical"

                elif "download_size" in data:
                    product_type = "digital"

                else:
                    raise ValueError(
                        "Missing product type and subclass attribute."
                    )

            # Preserve existing JSON validation rules
            if product_type == "physical" and "download_size" in data:
                raise ValueError(
                    "Physical product cannot have download_size."
                )

            if product_type == "digital" and "weight" in data:
                raise ValueError(
                    "Digital product cannot have weight."
                )

            # Factory handles product instantiation
            product = ProductFactory.create(
                product_type=product_type,
                product_id=data["id"],
                name=data["name"],
                price=data["price"],
                stock_quantity=data["stock"],
                supplier=supplier,
                weight=data.get("weight"),
                download_size=data.get("download_size")
            )

            if not inventory.add_product(product):
                print(
                    f"Skipped duplicate product ID: {product.product_id}"
                )

        except (KeyError, TypeError, ValueError, AttributeError):
            print("Skipped an invalid product in the inventory file.")

    return inventory

def save_inventory(inventory: Inventory, exit_save: bool = False) -> bool:
    try:
        with open(FILE_PATH, "w", encoding="utf-8") as file:
            json.dump(inventory.to_dict(), file, indent=4, allow_nan=False)
    except (OSError, UnicodeError, TypeError, ValueError) as error:
            print(f"Unable to save {FILE_NAME}: {error}")
            return False

    if exit_save:
        print("Inventory saved successfully.")
    else:
        print(f"Inventory saved successfully to {FILE_NAME}.")
    return True

