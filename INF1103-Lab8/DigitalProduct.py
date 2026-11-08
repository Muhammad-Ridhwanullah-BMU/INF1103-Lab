import math
from Product import Product
from Supplier import Supplier
class DigitalProduct(Product):
    def __init__(self, product_id:str, name:str, price:float, stock:int, supplier:Supplier, download_size: float) -> None:
        
        super().__init__(product_id, name, price, stock, supplier)

        if (isinstance(download_size, bool) or not isinstance(download_size, (int, float))
            or not math.isfinite(download_size)):
            raise ValueError("Download size must be a valid number.")
        
        if download_size < 0:
            raise ValueError("Download size cannot be negative.")
        
        self.__download_size = float(download_size)

    @property
    def download_size(self) -> float:
        return self.__download_size

    def to_dictionary(self) -> list[dict]:
        data = super().to_dictionary()
        data["type"] = "digital"
        data["download_size"] = self.__download_size
        return data

    def display_information(self) -> None:
        super().display_information()
        print(f"Download size: {self.__download_size:.2f}MB")
        print("Supplier Information: ")
        super().supplier_information()


    def display_summary(self) -> None:
        super().display_summary(end="")
        print(f" | Download Size: {self.__download_size:.2f} MB")
        print("Supplier Information: ")
        super().supplier_information()

    def get_fulfilment_info(self) -> str:
        return "This product is delivered digitally."