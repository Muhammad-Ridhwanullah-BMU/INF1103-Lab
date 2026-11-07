from Orderline import Orderline
from Product import Product

class Order():

    def __init__(self, order_id:str):

        if not isinstance(order_id, str) or not order_id.strip():
            raise ValueError("Order ID cannot be empty.")

        self.__order_id:str = order_id
        self.__order_lines:list[Orderline] = []

    def add_order_line(self, product:Product, quantity:int) -> None:
        order_line = Orderline(product, quantity)
        self.__order_lines.append(order_line)

    
