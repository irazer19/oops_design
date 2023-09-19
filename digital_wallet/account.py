import random
from wallet import Wallet
from enumerations import AccountStatus


class Account:
    def __init__(self, user, amount):
        self.__user = user
        self.__amount = amount
        self.__account_numer = None
        self.__wallet = None
        self.__status = AccountStatus.INACTIVE
        self.__available_acc_nums = [1, 2, 3, 4, 5]

    def create_wallet(self):
        w = Wallet(self.__amount)
        self.__wallet = w
        self.create_account_number()

    def create_account_number(self):
        self.__account_numer = random.choice(self.__available_acc_nums)
        self.__available_acc_nums.remove(self.__account_numer)
        self.set_active()

    def add_amount(self, amount):
        curr_amount = self.__wallet.get_amount()
        self.__wallet.set_amount(curr_amount + amount)

    def deduct_amount(self, amount):
        curr_amount = self.__wallet.get_amount()
        self.__wallet.set_amount(curr_amount - amount)

    def get_balance(self):
        return self.__wallet.get_amount()

    def set_active(self):
        self.__status = AccountStatus.ACTIVE

    def deactivate(self):
        self.__status = AccountStatus.INACTIVE

    def is_active(self):
        return self.__status == AccountStatus.ACTIVE

    def get_account_number(self):
        return self.__account_numer

    def get_account_stats(self):
        return {
            "acc_num": self.__account_numer,
            "name": self.__user.get_name(),
            "status": self.__status.name,
            "balance": self.get_balance(),
        }
