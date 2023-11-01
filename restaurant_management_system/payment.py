# Payment is an abstract class
from abc import ABC, abstractmethod


class Payment(ABC):
    def __init__(self, payment_id, creation_date, amount, status):
        self.__payment_id = payment_id
        self.__creation_date = creation_date
        self.__amount = amount
        self.status = status

    @abstractmethod
    def initiate_transaction(self):
        pass


class Check(Payment):
    def __init__(
        self, payment_id, creation_date, amount, status, bank_name, check_number
    ):
        super().__init__(payment_id, creation_date, amount, status)
        self.__bank_name = bank_name
        self.__check_number = check_number

    def initiate_transaction(self):
        pass


class CreditCard(Payment):
    def __init__(
        self, payment_id, creation_date, amount, status, name_on_card, zip_code
    ):
        super().__init__(payment_id, creation_date, amount, status)
        self.__name_on_card = name_on_card
        self.__zip_code = zip_code

    def initiate_transaction(self):
        pass


class Cash(Payment):
    def __init__(self, payment_id, creation_date, amount, status, cash_tendered):
        super().__init__(payment_id, creation_date, amount, status)
        self.__cash_tendered = cash_tendered

    def initiate_transaction(self):
        pass


class Bill:
    def __init__(self, bill_id, amount, tip, tax, is_paid):
        self.__bill_id = bill_id
        self.__amount = amount
        self.__tip = tip
        self.__tax = tax
        self.__is_paid = is_paid

    def generate_bill(self):
        pass
