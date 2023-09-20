# The Library is a singleton class that ensures it will have only one active instance at a time


class Library:
    def __init__(self, name, address):
        self.__name = name
        self.__address = address

    def get_address(self):
        pass
