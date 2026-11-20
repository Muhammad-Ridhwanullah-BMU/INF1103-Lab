import csv
from Inventory import Inventory
from Supplier import Supplier
from ProductFactory import ProductFactory

def load_products(
    path: str,
    inventory: Inventory,
    supplier: Supplier
) -> None:

    loaded = 0

    try:
        with open(path, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row_number, row in enumerate(reader, start=2):
                try:
                    product_type = row["product_type"].strip().lower()

                    # Lab-only defaults because CSV lacks these fields
                    extra = {}

                    if product_type == "physical":
                        extra["weight"] = 0.0

                    elif product_type == "digital":
                        extra["download_size"] = 0.0

                    product = ProductFactory.create(
                        product_type=product_type,
                        product_id=row["product_id"],
                        name=row["name"],
                        price=float(row["price"]),
                        stock_quantity=int(row["stock_quantity"]),
                        supplier=supplier,
                        **extra
                    )

                    if inventory.add_product(product):
                        loaded += 1
                    else:
                        print(
                            f"Skipped row {row_number}: "
                            "Duplicate product ID."
                        )

                except (ValueError, TypeError, KeyError, AttributeError) as error:
                    print(f"Skipped row {row_number}: {error}")

        print(f"Loaded {loaded} product(s).")

    except FileNotFoundError:
        print(f"Products file not found: {path}")

    except (OSError, csv.Error) as error:
        print(f"Unable to read products: {error}")

    finally:
        print("Load attempt finished.")
