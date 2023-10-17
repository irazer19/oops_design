from abc import ABC, abstractmethod


class Search(ABC):
    def search_by_type(self, type):
        pass

    def search_by_model(self, model):
        pass


class VehicleCatalog(Search):
    def __init__(self):
        self.__vehicle_types = {}
        self.__vehicle_models = {}

    # to return all vehicles of the given type.
    def search_by_type(self, type):
        pass

    # to return all vehicles of the given model.
    def search_by_model(self, model):
        pass
