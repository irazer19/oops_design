class Team:
    def __init__(self, name, players, coach, news, stats):
        self.__name = name
        self.__players = players
        self.__coach = coach
        self.__news = news
        self.__stats = stats

    def add_squad(self, squad):
        pass

    def add_player(self, player):
        pass

    def add_news(self, news):
        pass


class TournamentSquad:
    def __init__(self, players, tournament, stats):
        self.__players = players
        self.__tournament = tournament
        self.__stats = stats

    def add_player(self, player):
        pass


class Playing11:
    def __init__(self, players):
        self.__players = players

    def add_player(self, player):
        pass
