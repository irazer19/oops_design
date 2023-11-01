from abc import ABC, abstractmethod


class Account:
    def __init__(self, account_id, password, address, status):
        self.__account_id = account_id
        self.__password = password
        self.__address = address
        self.__status = status  # Refers to the AccountStatus enum

    def reset_password(self):
        pass


class Person(ABC):
    def __init__(self, name, email, phone_number):
        self.__name = name
        self.__email = email
        self.__phone_number = phone_number


class Customer(Person):
    def __init__(self, name, email, phone_number, last_visited_date):
        super().__init__(name, email, phone_number)
        self.__last_visited_date = last_visited_date


class Employee(Person):
    def __init__(self, name, email, phone_number, employee_id, joining_date):
        super().__init__(name, email, phone_number)
        self.__employee_id = employee_id
        self.__joining_date = joining_date


class Chef(Employee):
    def prepare_order(self):
        pass


class Waiter(Employee):
    def take_order(self):
        pass


class Manager(Employee):
    def add_employee(self):
        pass


class Receptionist(Employee):
    def create_reservation(self):
        pass
