from abc import ABC, abstractmethod


class OrderPart:
    def __init__(self, price, quantity, executed_at):
        self.__price = price
        self.__quantity = quantity
        self.__executed_at = executed_at


class Order(ABC):
    def __init__(
        self, order_number, is_buy_order, status, time_enforcement, creation_time
    ):
        self.__order_number = order_number
        self.__is_buy_order = is_buy_order
        self.__status = status
        self.__time_enforcement = time_enforcement
        self.__creation_time = creation_time
        self.__parts = {}

    def set_status(self, OrderStatus, status):
        pass

    def save_in_database(self):
        pass

    def add_order_parts(self, OrderParts, parts):
        pass


# Types of Orders
class LimitOrder(Order):
    def __init__(
        self, order_number, is_buy_order, status, time_enforcement, creation_time
    ):
        super().__init__(
            order_number, is_buy_order, status, time_enforcement, creation_time
        )


class StopLimitOrder(Order):
    def __init__(
        self, order_number, is_buy_order, status, time_enforcement, creation_time
    ):
        super().__init__(
            order_number, is_buy_order, status, time_enforcement, creation_time
        )


class StopLossOrder(Order):
    def __init__(
        self, order_number, is_buy_order, status, time_enforcement, creation_time
    ):
        super().__init__(
            order_number, is_buy_order, status, time_enforcement, creation_time
        )


class MarketOrder(Order):
    def __init__(
        self, order_number, is_buy_order, status, time_enforcement, creation_time
    ):
        super().__init__(
            order_number, is_buy_order, status, time_enforcement, creation_time
        )
