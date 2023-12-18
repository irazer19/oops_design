from abc import ABC, abstractmethod


class Search(ABC):
    def search_by_tags(self, name):
        pass

    def search_by_users(self, name):
        pass

    def search_by_words(self, words):
        pass


class SearchCatalog(Search):
    def __init__(self):
        self.__questions_using_tags = {}
        self.__questions_using_users = {}
        self.__questions_using_words = {}

    def search_by_tags(self, name):
        # functionality
        pass

    def search_by_users(self, name):
        # functionality
        pass

    def search_by_words(self, words):
        # functionality
        pass
