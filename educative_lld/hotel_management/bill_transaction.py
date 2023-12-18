# BillTransaction is an abstract class
from abc import ABC, abstractmethod


class BillTransaction(ABC):
    def __init__(self, creation_date, amount, status):
        self.__creation_date = creation_date
        self.__amount = amount
        self.status = status

    @abstractmethod
    def initiate_transaction(self):
        pass


class CheckTransaction(BillTransaction):
    def __init__(self, creation_date, amount, status, bank_name, check_number):
        super().__init__(creation_date, amount, status)
        self.__bank_name = bank_name
        self.__check_number = check_number

    def initiate_transaction(self):
        pass


class CreditCardTransaction(BillTransaction):
    def __init__(self, creation_date, amount, status, name_on_card, zip_code):
        super().__init__(creation_date, amount, status)
        self.__name_on_card = name_on_card
        self.__zip_code = zip_code

    def initiate_transaction(self):
        pass


class CashTransaction(BillTransaction):
    def __init__(self, creation_date, amount, status, cash_tendered):
        super().__init__(creation_date, amount, status)
        self.__cash_tendered = cash_tendered

    def initiate_transaction(self):
        pass
