class Admin:
    def __init__(self):
        pass

    def add_player(self, player):
        pass

    def add_team(self, team):
        pass

    def add_match(self, match):
        pass

    def add_tournament(self, tournament):
        pass

    def add_stats(self, stats):
        pass

    def add_news(self, news):
        pass


class Player:
    def __init__(self, name, age, country, position, teams, stat):
        self.__namer = name
        self.__age = age
        self.__country = country
        self.__position = position
        self.__teams = teams
        self.__stat = stat


class Coach:
    def __init__(self, name, age, country, teams):
        self.__namer = name
        self.__age = age
        self.__country = country
        self.__teams = teams


class Umpire:
    def __init__(self, name, age, country):
        self.__namer = name
        self.__age = age
        self.__country = country

    def assign_match(self, match):
        pass
