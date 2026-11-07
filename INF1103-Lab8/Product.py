import math
from abc import ABC, abstractmethod
from Supplier import Supplier
class Product(ABC):

    def __init__(self, product_id:str, name:str, price:float, stock:int, supplier:Supplier):
        
        if not isinstance(product_id, str) or not product_id.strip():
            raise ValueError("Product ID cannot be empty.")
        
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Product name cannot be empty.")
        
        if (isinstance(price, bool) or not isinstance(price, (int, float))
                or not math.isfinite(price)):
            raise ValueError("Price must be a valid number.")
        
        if isinstance(stock, bool) or not isinstance(stock, int):
            raise ValueError("Stock must be a whole number.")
        
        if price < 0 or stock < 0:
            raise ValueError("Price and stock cannot be negative.")
        
        if not isinstance(supplier, Supplier):
            raise ValueError("Supplier is needed.")
        

        self.__product_id:str = product_id.strip()
        self.__name:str = name.strip()
        self.__price:float = float(price)
        self.__stock:int = stock
        self.__supplier:Supplier = supplier

    @property
    def product_id(self) -> str:
        return self.__product_id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def price(self) -> float:
        return self.__price

    @property
    def stock(self) -> int:
        return self.__stock

    def display_summary(self, end="\n") -> None:
        print(
            f"ID: {self.__product_id} | "
            f"Name: {self.__name} | "
            f"Price: ${self.__price:.2f} | "
            f"Stock: {self.__stock}",
            end=end
        )

    def display_information(self) -> None:
        print(f"ID: {self.__product_id}")
        print(f"Name: {self.__name}")
        print(f"Price: ${self.__price:.2f}")
        print(f"Stock: {self.__stock}")

    def supplier_information(self) -> None:
        self.__supplier.supplier_information()

    def update_stock(self, quantity) -> None:
        if isinstance(quantity, bool) or not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Stock must be a non-negative whole number.")
        self.__stock = quantity

    @abstractmethod
    def get_fulfilment_info(self) -> str:
        pass

    def to_dictionary(self) -> dict:
        return {
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock,
        }