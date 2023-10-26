# Customer is an abstract class
from abc import ABC, abstractmethod


class Customer(ABC):
    def __init__(self, cart, order):
        self.__cart = cart  # Refers to an instance of the ShoppingCart class

    # Returns the ShoppingCart class
    @abstractmethod
    def get_shopping_cart(self):
        pass


class Guest(Customer):
    def __init__(self, cart, order):
        super().__init__(cart, order)

    def register_account(self):
        pass

    # Returns the ShoppingCart class
    def get_shopping_cart(self):
        # Add functionality
        pass


class AuthenticatedUser(Customer):
    def __init__(self, account, cart, order):
        self.__account = account  # Refers to an instance of the Account class
        self.__order = order  # Refers to an instance of the Order class
        super().__init__(cart, order)

    # order here refers to an instance of the Order class
    # Returns a value from the OrderStatus enum
    def place_order(self, order):
        pass

    # Returns the ShopppingCart class
    def get_shopping_cart(self):
        # Add functionality
        pass
