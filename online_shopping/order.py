class Order:
    def __init__(self, order_number, status, order_date, order_log, shopping_cart):
        self.__order_number = order_number
        self.__status = status  # Refers to the OrderStatus enum
        self.__order_date = order_date
        self.__order_log = order_log  # List of order logs
        self.__shopping_cart = shopping_cart

    def send_for_shipment(self):
        pass

    # payment here refers to an instance of the Payment class
    def make_payment(self, payment):
        pass

    # order_log here refers to an instance of the OrderLog class
    def add_order_log(self, order_log):
        pass


class OrderLog:
    def __init__(self, order_number, creation_date, status):
        self.__order_number = order_number
        self.__creation_date = creation_date
        self.__status = status  # Refers to the OrderStatus enum
