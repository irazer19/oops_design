from abc import ABC, abstractmethod


class Search(ABC):
    # Returns list of movie titles
    @abstractmethod
    def search_movie_title(self, title):
        pass

    # Returns list of movie languages
    @abstractmethod
    def search_movie_language(self, language):
        pass

    # Returns list of movie genres
    @abstractmethod
    def search_movie_genre(self, genre):
        pass

    # Returns list of movie release dates
    @abstractmethod
    def search_movie_release_date(self, date):
        pass


class Catalogue(Search):
    def __init__(self):
        self.__movie_titles = {}
        self.__movie_languages = {}
        self.__movie_genres = {}
        self.__movie_release_dates = {}

    # Returns list of movie titles
    def search_movie_title(self, title):
        # functionality
        pass

    # Returns list of movie languages
    def search_movie_language(self, language):
        # functionality
        pass

    # Returns list of movie genres
    def search_movie_genre(self, genre):
        # functionality
        pass

    # Returns list of movie release dates
    def search_movie_release_date(self, date):
        # functionality
        pass
