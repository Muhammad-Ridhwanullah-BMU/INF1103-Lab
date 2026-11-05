class Inventory:

    def __init__(self):
        self.__products = []

    @property    
    def products(self):
        return self.__products.copy()

    def display_all(self):
        print("Current Inventory")
        print("------------------------------------------------")

        if not self.__products:
            print("No products in inventory.")
        else:
            for product in self.__products:
                product.display_summary()

        print("------------------------------------------------")

    def add_product(self, product):
        if self.search_product(product.product_id) is not None:
            return False

        self.__products.append(product)
        return True
    
    #Returns a matching Product or None
    def search_product(self, product_id):
        for product in self.__products:
            if product.product_id.lower() == product_id.lower():
                return product
        return None

    def to_dict(self):
        return [product.to_dictionary() for product in self.__products]