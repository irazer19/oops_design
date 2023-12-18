class Address:
    def __init__(self, street_address, city, state, zip_code, country):
        self.__street_address = street_address
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code
        self.__country = country


class Person:
    def __init__(self, name, address, email, phone_number):
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone_number = phone_number


class Driver(Person):
    def __init__(self, name, address, email, phone_number, driver_id):
        super().__init__(name, address, email, phone_number)
        self.__driver_id = driver_id
