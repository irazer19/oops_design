from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, id, password, name, address, email, phone):
        self.__id = id
        self.__password = password
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone
        self.__status = None

    @abstractmethod
    def reset_password(self):
        pass


class Member(Account):
    def __init__(self, id, password, name, address, email, phone):
        super().__init__(id, password, name, address, email, phone)
        self.__available_funds_for_trading = 0.0
        self.__date_of_membership = None
        self.__stock_positions = {}
        self.__active_orders = {}

    def place_sell_limit_order(self, stock_id, quantity, limit_price, enforcement_type):
        pass

    def place_buy_limit_order(self, stock_id, quantity, limit_price, enforcement_type):
        pass

    def callback_stock_exchange(self, order_id, order_parts, status):
        pass

    def reset_password(self):
        pass


# functionality


class Admin(Account):
    def block_member(self):
        pass

    def unblock_member(self):
        pass

    def cancel_membership(self):
        pass

    def reset_password(self):
        pass


# functionality
