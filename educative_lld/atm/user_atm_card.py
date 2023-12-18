class User:
    def __init__(self, card, account):
        self.__card = card
        self.__account = account


class ATMCard:
    def __init__(self, cardNumber, customerName, cardExpiryDate, pin):
        self.__cardNumber = cardNumber
        self.__customerName = customerName
        self.__cardExpiryDate = cardExpiryDate
        self.__pin = pin
