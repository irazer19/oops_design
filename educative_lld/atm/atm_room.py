class ATM:
    def __init__(
        self,
        currentATMState,
        atmBalance,
        noOfHundredDollarBills,
        noOfFiftyDollarBills,
        noOfTenDollarBills,
    ):
        self.__currentATMState = currentATMState
        self.atmBalance = atmBalance
        self.noOfHundredDollarBills = noOfHundredDollarBills
        self.noOfFiftyDollarBills = noOfFiftyDollarBills
        self.noOfTenDollarBills = noOfTenDollarBills

    def displayCurrentState(self):
        pass

    def initializeATM(
        self,
        atmBalance,
        noOfHundredDollarBills,
        noOfFiftyDollarBills,
        noOfTenDollarBills,
    ):
        pass


class ATMRoom:
    def __init__(self, atm, user):
        self.__atm = atm
        self.user = user
