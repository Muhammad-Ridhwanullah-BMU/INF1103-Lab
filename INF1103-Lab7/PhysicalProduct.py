import math
from Product import Product
from CanBeShipped import CanBeShipped
class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        if (isinstance(weight, bool) or not isinstance(weight, (int, float))
            or not math.isfinite(weight)):
            raise ValueError("Weight must be a valid number.")
        if weight < 0:
            raise ValueError("Weight cannot be negative.")
        self.__weight = float(weight)

    @property
    def weight(self):
        return self.__weight

    def to_dictionary(self):
        data = super().to_dictionary()
        data["type"] = "physical"
        data["weight"] = self.__weight
        return data