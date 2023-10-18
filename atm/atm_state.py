from abc import ABC, abstractmethod


class ATMState(ABC):
    @abstractmethod
    def insertCard(self, atm, card):
        pass

    @abstractmethod
    def authenticatePin(self, atm, card, pin):
        pass

    @abstractmethod
    def selectOperation(self, atm, card, transactionType):
        pass

    @abstractmethod
    def cashWithdrawal(self, atm, card, withdrawAmount):
        pass

    @abstractmethod
    def displayBalance(self, atm, card):
        pass

    @abstractmethod
    def transferMoney(self, atm, card, accountNumber, transferAmount):
        pass

    @abstractmethod
    def returnCard(self):
        pass

    @abstractmethod
    def exit(self, atm):
        pass


class IdleState(ATMState):
    def insertCard(self, atm, card):
        pass

    def returnCard(self):
        pass

    # all other methods are implemented

    def exit(self, atm):
        pass


class HasCardState(ATMState):
    def authenticatePin(self, atm, card, pin):
        pass

    def returnCard(self):
        pass

    def exit(self, atm):
        pass


class SelectOperationState(ATMState):
    def selectOperation(self, atm, card, transactionType):
        pass

    def returnCard(self):
        pass

    def exit(self, atm):
        pass


class CheckBalanceState(ATMState):
    def displayBalance(self, atm, card):
        pass

    def returnCard(self):
        pass

    def exit(self, atm):
        pass


class CashWithdrawalState(ATMState):
    def cashWithdrawal(self, atm, card, withdrawAmount):
        pass

    def returnCard(self):
        pass

    def exit(self, atm):
        pass


class TransferMoneyState(ATMState):
    def transferMoney(self, atm, card, accountNumber, transferAmount):
        pass

    def returnCard(self):
        pass

    def exit(self, atm):
        pass
