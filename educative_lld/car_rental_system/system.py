class CarRentalBranch:
    def __init__(self, name, address):
        self.__name = name
        self.__address = address
        self.__stalls = []

    def get_location(self):
        return self.__address


class __CarRentalSystem(object):
    __instances = None

    def __new__(cls):
        if cls.__instances is None:
            cls.__instances = super(__CarRentalSystem, cls).__new__(cls)
        return cls.__instances


class CarRentalSystem(metaclass=__CarRentalSystem):
    def __init__(self, name):
        self.__name = name
        self.__branches = []

    def add_new_branch(self, branch):
        pass
