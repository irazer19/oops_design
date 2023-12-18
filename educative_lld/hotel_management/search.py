from abc import ABC, abstractmethod


class Search(ABC):
    def search(self, style, start_date, duration):
        pass


class Catalog(Search):
    def __init__(self):
        self.__rooms = []

    def search(self, style, date, duration):
        pass
