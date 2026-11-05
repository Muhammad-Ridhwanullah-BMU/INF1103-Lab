import math
from Product import Product
class DigitalProduct(Product):
    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        if (isinstance(download_size, bool) or not isinstance(download_size, (int, float))
            or not math.isfinite(download_size)):
            raise ValueError("Download size must be a valid number.")
        if download_size < 0:
            raise ValueError("Download size cannot be negative.")
        self.__download_size = float(download_size)

    @property
    def download_size(self):
        return self.__download_size

    def to_dictionary(self):
        data = super().to_dictionary()
        data["type"] = "digital"
        data["download_size"] = self.__download_size
        return data

    def display_information(self):
        super().display_information()
        print(f"Download size: {self.__download_size:.2f}MB")

    def display_summary(self):
        super().display_summary(end="")
        print(f" | Download Size: {self.__download_size:.2f} MB")

    def get_fulfilment_info(self):
        return "This product is delivered digitally."