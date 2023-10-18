from abc import ABC, abstractmethod


class Bank:
    def __init__(self, name, bankCode, availableBalance):
        self.__name = name
        self.__bankCode = bankCode
        self.__availableBalance = availableBalance

    def getBankCode(self):
        pass

    def addATM(self):
        pass


class BankAccount:
    def __init__(self, accountNumber, totalBalance, availableBalance):
        self.__accountNumber = accountNumber
        self.__totalBalance = totalBalance
        self.__availableBalance = availableBalance

    def getAvailableBalance(self):
        pass


class SavingAccount(BankAccount):
    def __init__(self, accountNumber, totalBalance, availableBalance):
        super().__init__(accountNumber, totalBalance, availableBalance)

    def withdrawLimit(self):
        pass


class CurrentAccount(BankAccount):
    def __init__(self, accountNumber, totalBalance, availableBalance):
        super().__init__(accountNumber, totalBalance, availableBalance)

    def withdrawLimit(self):
        pass
