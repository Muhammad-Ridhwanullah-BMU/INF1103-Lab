from Product import Product
class Orderline():

    def __init__(self, product:Product, quantity:int):
            if not isinstance(product, Product):
                raise ValueError("Product is needed.")
            if isinstance(quantity, bool) or not isinstance(quantity, int):
                raise ValueError("Quantity must be a whole number.")

            self.__product:Product = product
            self.__quantity:int = quantity

    def calculate_subtotal(self) -> float:
        return self.__product.price * self.__quantity