from OrderLine import OrderLine
from Product import Product

class Order():

    def __init__(self, order_id:str) -> None:

        if not isinstance(order_id, str) or not order_id.strip():
            raise ValueError("Order ID cannot be empty.")

        self.__order_id:str = order_id.strip()
        self.__order_lines:list[OrderLine] = []

    @property
    def order_lines(self) -> list[OrderLine]:
        return self.__order_lines.copy()

    @property
    def order_id(self) -> str:
        return self.__order_id

    def add_order_line(self, product:Product, quantity:int) -> None:
        order_line = OrderLine(product, quantity)
        self.__order_lines.append(order_line)

    def calculate_total(self) -> float:
        total = 0.0
        
        for orderlines in self.__order_lines:
            total += orderlines.calculate_subtotal()

        return total

    def display_order_lines(self) -> None:
        print(f"Order {self.__order_id}")
        if not self.__order_lines:
            print("No order lines.")
        else:
            for order_line in self.__order_lines:
                order_line.display_information()