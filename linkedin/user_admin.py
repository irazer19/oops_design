from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, address, email, phone, account):
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone
        self.__account = account


# Admin extends Person
class Admin(Person):
    def __init__(self, name, address, email, phone, account):
        super().__init__(name, address, email, phone, account)

    def block_user(self, user):
        pass

    def unblock_user(self, user):
        pass

    def disable_page(self, page):
        pass

    def enable_page(self, page):
        pass

    def delete_group(self, group):
        pass


# User extends Person
class User(Person):
    def __init__(
        self, name, address, email, phone, account, user_id, date_of_joining, profile
    ):
        self.__user_id = user_id
        self.date_of_joining = date_of_joining
        self.__profile = profile
        self.__connections = []
        self.__follows_users = []
        self.__follows_companies = []
        self.__joined_groups = []
        self.__created_pages = []
        self.__created_groups = []
        super().__init__(name, address, email, phone, account)

    def send_message(self, message):
        pass

    def send_invite(self, invite):
        pass

    def cancel_invite(self, invite):
        pass

    def create_page(self, page):
        pass

    def delete_page(self, page):
        pass

    def create_group(self, group):
        pass

    def delete_group(self, group):
        pass

    def create_post(self, post):
        pass

    def delete_post(self, post):
        pass

    def create_comment(self, comment):
        pass

    def delete_comment(self, comment):
        pass

    def react(self, post):
        pass

    def request_recommendation(self, user):
        pass

    def accept_recommendation(self, user):
        pass

    def apply_for_job(self, job):
        pass
