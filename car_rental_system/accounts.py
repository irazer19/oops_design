from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(
        self, name, address, email, phone_number, account_id, password, person
    ):
        self.__id = account_id
        self.__password = password
        self.__status = None
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone_number = phone_number
        self.__person = person

    @abstractmethod
    def reset_password(self):
        pass


class Receptionist(Account):
    def __init__(
        self,
        name,
        address,
        email,
        phone_number,
        account_id,
        password,
        person,
        date_joined,
    ):
        super().__init__(
            name, address, email, phone_number, account_id, password, person
        )
        self.__date_joined = date_joined

    def search_customer(self, name):
        pass

    def add_reservation(self):
        pass

    def cancel_reservation(self):
        pass

    def reset_password(self):
        pass


# functionality


class Customer(Account):
    def __init__(
        self,
        name,
        address,
        email,
        phone_number,
        account_id,
        password,
        person,
        license_number,
        lisense_expiry,
    ):
        super().__init__(
            name, address, email, phone_number, account_id, password, person
        )
        self.__license_number = license_number
        self.__lisense_expiry = lisense_expiry

    def add_reservation(self):
        pass

    def cancel_reservation(self):
        pass

    def get_reservations(self):
        pass

    def reset_password(self):
        pass


# functionality
