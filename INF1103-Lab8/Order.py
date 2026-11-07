from Orderline import Orderline

class Order():

    def __init__(self, order_id:str):

        if not isinstance(order_id, str) or not order_id.strip():
            raise ValueError("Order ID cannot be empty.")

        self.__order_id:str = order_id
        self.__orderlines:list[Orderline] = []