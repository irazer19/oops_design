from abc import ABC, abstractmethod


class Search(ABC):
    def search_user(self, name):
        pass

    def search_company(self, name):
        pass

    def search_group(self, name):
        pass

    def search_job(self, title):
        pass


class SearchCatalog(Search):
    def __init__(self):
        self.__users = {}
        self.__companies = {}
        self.__groups = {}
        self.__jobs = {}

    def add_new_user(self, user):
        pass

    def add_new_company(self, company):
        pass

    def add_new_group(self, group):
        pass

    def add_new_job(self, job):
        pass

    def search_user(self, name):
        # functionality
        pass

    def search_company(self, name):
        # functionality
        pass

    def search_group(self, name):
        # functionality
        pass

    def search_job(self, title):
        # functionality
        pass


class Notification:
    def __init__(self, notification_id, created_on, content):
        self.__notification_id = notification_id
        self.__created_on = created_on
        self.__content = content

    # account here refers to the Account class
    def send_notification(self, account):
        pass
