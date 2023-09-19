class User:
    def __init__(self, name, email):
        self.__name = name
        self.__email = email

    def get_name(self):
        return self.__name
