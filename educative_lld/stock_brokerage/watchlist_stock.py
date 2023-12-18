class Watchlist:
    def __init__(self, name, stocks):
        self.__name = name
        self.__stocks = stocks

    def get_stocks(self):
        pass


class Stock:
    def __init__(self, symbol, price):
        self.__symbol = symbol
        self.__price = price
