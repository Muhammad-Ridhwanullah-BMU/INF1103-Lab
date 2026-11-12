from Product import Product
class OrderLine():

    def __init__(self, product:Product, quantity:int) -> None:
            if not isinstance(product, Product):
                raise ValueError("Product is needed.")
            if isinstance(quantity, bool) or not isinstance(quantity, int) or quantity <= 0:
                raise ValueError("Quantity must be a positive whole number.")

            self.__product:Product = product
            self.__quantity:int = quantity

    @property
    def product(self) -> Product:
        return self.__product
    
    @property
    def quantity(self) -> int:
        return self.__quantity 

    def calculate_subtotal(self) -> float:
        return self.__product.price * self.__quantity

    def display_information(self) -> None:
        print(
            f"Product: {self.__product.product_id} ({self.__product.name}) | "
            f"Quantity: {self.__quantity} | "
            f"Subtotal: ${self.calculate_subtotal():.2f}"
        )
        
