import math
from Product import Product
from CanBeShipped import CanBeShipped
from Supplier import Supplier
class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id:str, name:str, price:float, stock:int, supplier:Supplier, weight:float) -> None:
        
        super().__init__(product_id, name, price, stock, supplier)
        
        if (isinstance(weight, bool) or not isinstance(weight, (int, float))
            or not math.isfinite(weight)):
            raise ValueError("Weight must be a valid number.")
        
        if weight < 0:
            raise ValueError("Weight cannot be negative.")
        
        self.__weight = float(weight)

    @property
    def weight(self) -> float:
        return self.__weight

    def to_dictionary(self) -> dict:
        data = super().to_dictionary()
        data["type"] = "physical"
        data["weight"] = self.__weight
        return data

    def display_information(self) -> None:
        super().display_information()
        print(f"Weight: {self.__weight:.2f}KG")
        print("Supplier Information: ")
        super().supplier_information()

    def display_summary(self, end="\n") -> None:
        super().display_summary(end="")
        print(f" | Weight: {self.__weight:.2f} KG")
        print("Supplier Information: ")
        super().supplier_information()
        print(end=end)

    def get_fulfilment_info(self) -> str:
        return "This product is delivered through physical courier shipping."

    def calculate_shipping_cost(self) -> float:
        cost = 0.82 if self.__weight <= 0.5 else 2.00 if self.__weight <= 2 else 5.00
        print(f"The cost of shipping will be ${cost:.2f}")
        return cost