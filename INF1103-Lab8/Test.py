from DigitalProduct import DigitalProduct
from Inventory import Inventory
from Order import Order
from PhysicalProduct import PhysicalProduct
from Product import Product
from Supplier import Supplier

# S.6.2
def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfilment_info())

#7
def test_polymorphism() -> None:
    supplier = Supplier("S001", "ABC Store", "abc@example.com")
    physical = PhysicalProduct("P001", "Laptop", 1200, 10, supplier, 2.5)
    digital = DigitalProduct("D001", "E-Book", 25, 100, supplier, 5.0)

    inventory = Inventory()
    assert inventory.add_product(physical)
    assert inventory.add_product(digital)

    # No isinstance() or type() checks: both use the same Product interface.
    for product in inventory.products:
        print("----------------------------------------")
        show_product_details(product)

    # Verify that the two implementations return their expected messages.
    assert physical.get_fulfilment_info() == (
        "This product is delivered through physical courier shipping."
    )
    assert digital.get_fulfilment_info() == (
        "This product is delivered digitally."
    )

    # Both products can be found and managed using the parent class interface.
    assert inventory.find_product("P001") is physical
    assert inventory.find_product("D001") is digital
    physical.update_stock(8)
    digital.update_stock(90)
    assert physical.stock == 8
    assert digital.stock == 90

    print("----------------------------------------")
    print("Section 7 polymorphism and LSP test passed.")


def main() -> None:
    supplier = Supplier("S001", "Example Shop", "shop@example.com")
    physical = PhysicalProduct("P001", "Laptop", 1200, 15, supplier, 2.5)
    digital = DigitalProduct("P002", "E-Book", 25, 100, supplier, 5.0)

    print("\n=== SECTION 2: ASSOCIATION ===")
    print("Prediction: deleting the supplier variable will not destroy the Supplier.")
    print("Same Supplier object:", physical.supplier is digital.supplier)
    del supplier
    physical.supplier_information()
    digital.supplier_information()

    print("\n=== SECTION 3: AGGREGATION ===")
    print("Prediction: Product survives removal from Inventory A.")
    inventory_a = Inventory()
    inventory_a.add_product(physical)
    inventory_a.remove_product("P001")
    print("Inventory A no longer holds Product:", inventory_a.find_product("P001") is None)
    physical.display_summary()
    inventory_b = Inventory()
    inventory_b.add_product(physical)
    print("Inventory B holds same Product:", inventory_b.find_product("P001") is physical)

    print("\n=== SECTION 4: COMPOSITION ===")
    print("Prediction: two different OrderLines, one shared Product.")
    order_a = Order("O001")
    order_b = Order("O002")
    order_a.add_order_line(physical, 2)
    order_a.add_order_line(digital, 1)
    order_b.add_order_line(physical, 3)
    line_a = order_a.order_lines[0]
    line_b = order_b.order_lines[0]
    print("Different OrderLine objects:", line_a is not line_b)
    print("Same Product object:", line_a.product is line_b.product)
    order_a.display_order_lines()
    print(f"Order A total: ${order_a.calculate_total():.2f}")
    order_b.display_order_lines()
    print(f"Order B total: ${order_b.calculate_total():.2f}")
    del line_a, line_b  # Release inspection references before deleting Order A
    del order_a
    print("Product still exists after deleting Order A:", physical.name)

    print("\n=== SECTION 6: LSP ===")
    show_product_details(physical)
    show_product_details(digital)
    inventory_b.add_product(digital)
    inventory_b.display_all_products()
    physical.update_stock(20)
    digital.update_stock(20)
    print("Both stocks updated:", physical.stock == digital.stock == 20)

    print("\n=== SECTION 7: POLYMORPH ===")
    test_polymorphism()

if __name__ == "__main__":
    main()