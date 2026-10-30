class Inventory:

    def __init__(self):
        self.__products = []
        
    def get_products(self):
        return self.__products.copy()
