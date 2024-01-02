from abc import ABC, abstractmethod


class State(ABC):
    def __init__(self, atm):
        self.atm = atm

    @abstractmethod
    def insert_card(self, atm, card):
        pass

    @abstractmethod
    def authenticate_pin(self, pin):
        pass

    @abstractmethod
    def exit(self):
        pass

    @abstractmethod
    def return_card(self):
        pass

    @abstractmethod
    def select_operation(self, op):
        pass

    @abstractmethod
    def withdraw_cash(self, amount):
        pass

    @abstractmethod
    def display_balance(self):
        pass


class IdleState(State):
    def __init__(self):
        super().__init__(None)

    def insert_card(self, atm, card):
        atm.add_card(card)
        atm.state = HasCardState(atm)

    def authenticate_pin(self, pin):
        pass

    def exit(self):
        pass

    def return_card(self):
        pass

    def select_operation(self, op):
        pass

    def withdraw_cash(self, amount):
        pass

    def display_balance(self):
        pass


class HasCardState(State):
    def __init__(self, atm):
        super().__init__(atm)

    def insert_card(self, atm, card):
        pass

    def authenticate_pin(self, pin):
        if pin == self.atm.card.pin:
            self.atm.state = SelectionState(self.atm)
            print("Pin verified.")
        else:
            print("Wrong pin")
            self.atm.state = IdleState()

    def exit(self):
        self.return_card()
        self.atm.state = IdleState()

    def return_card(self):
        self.atm.remove_card()

    def select_operation(self, op):
        pass

    def withdraw_cash(self, amount):
        pass

    def display_balance(self):
        pass


class SelectionState(State):
    def __init__(self, atm):
        super().__init__(atm)

    def insert_card(self, atm, card):
        pass

    def authenticate_pin(self, pin):
        pass

    def exit(self):
        self.return_card()
        self.atm.state = IdleState()

    def return_card(self):
        self.atm.remove_card()

    def select_operation(self, op):
        if op == "WITHDRAW":
            self.atm.state = CashWithdrawalState(self.atm)
        elif op == "SHOW_BALANCE":
            self.atm.state = DisplayBalanceState(self.atm)

    def withdraw_cash(self, amount):
        pass

    def display_balance(self):
        pass


class CashWithdrawalState(State):
    def __init__(self, atm):
        super().__init__(atm)

    def insert_card(self, atm, card):
        pass

    def authenticate_pin(self, pin):
        pass

    def exit(self):
        self.return_card()
        self.atm.state = IdleState()

    def return_card(self):
        self.atm.remove_card()

    def select_operation(self, op):
        pass

    def withdraw_cash(self, amount):
        print(f"Deducted amount {amount}")
        # Deduct the amount from the user bank account
        # We can also use Chain of responsibility design pattern here using WithdrawCashProcessor class to
        # process 2000, 500, 100 notes in order.
        pass

    def display_balance(self):
        pass


class DisplayBalanceState(State):
    def __init__(self, atm):
        super().__init__(atm)

    def insert_card(self, atm, card):
        pass

    def authenticate_pin(self, pin):
        pass

    def exit(self):
        self.return_card()
        self.atm.state = IdleState()

    def return_card(self):
        self.atm.remove_card()

    def select_operation(self, op):
        pass

    def withdraw_cash(self, amount):
        pass

    def display_balance(self):
        print(f"Your account balance is Rs: {self.atm.card.bank_account.balance}")
