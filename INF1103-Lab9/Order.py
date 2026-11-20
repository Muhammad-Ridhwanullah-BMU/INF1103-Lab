from OrderLine import OrderLine
from Product import Product
from DiscountStrategy import DiscountStrategy
from NoDiscount import NoDiscount

class Order():

    def __init__(self, order_id:str, discount:DiscountStrategy) -> None:

        if not isinstance(order_id, str) or not order_id.strip():
            raise ValueError("Order ID cannot be empty.")

        self.__order_id:str = order_id.strip()
        self.__order_lines:list[OrderLine] = []
        self.discount: DiscountStrategy = NoDiscount()

        if discount is not None:
            self.set_discount(discount)

    @property
    def order_lines(self) -> list[OrderLine]:
        return self.__order_lines.copy()

    @property
    def order_id(self) -> str:
        return self.__order_id

    def set_discount(self, discount: DiscountStrategy  | None = None) -> None:
        if not isinstance(discount, DiscountStrategy):
            raise TypeError("Discount must be a DiscountStrategy.")

        self.discount = discount

    def add_order_line(self, product:Product, quantity:int) -> None:
        order_line = OrderLine(product, quantity)
        self.__order_lines.append(order_line)

    def calculate_total(self) -> float:
        total = 0.0
        
        for orderlines in self.__order_lines:
            total += orderlines.calculate_subtotal()

        return self.discount.apply(total)

    def display_order_lines(self) -> None:
        print(f"Order {self.__order_id}")
        if not self.__order_lines:
            print("No order lines.")
        else:
            for order_line in self.__order_lines:
                order_line.display_information()
