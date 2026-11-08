from Product import Product
class Inventory:

    def __init__(self) -> None:
        self.__products: list[Product] = []

    @property    
    def products(self) -> list[Product]:
        return self.__products.copy()

    def display_all(self) -> None:
        print("Current Inventory")
        print("------------------------------------------------")

        if not self.__products:
            print("No products in inventory.")
        else:
            for product in self.__products:
                product.display_summary()

        print("------------------------------------------------")

    def add_product(self, product:Product) -> bool:
        if self.find_product(product.product_id) is not None:
            return False

        self.__products.append(product)
        return True
    
    #Returns a matching Product or None
    def find_product(self, product_id:str) -> Product | None:
        for product in self.__products:
            if product.product_id.lower() == product_id.lower():
                return product
        return None

    def remove_product(self, product_id:str) -> bool:
        product = self.find_product(product_id)
        if product is None:
            return False
        
        self.__products.remove(product)
        return True

    def to_dict(self) -> list[dict]:
        return [product.to_dictionary() for product in self.__products]