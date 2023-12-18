class Tournament:
    def __init__(self, start_date, teams, matches, points):
        self.__start_date = start_date
        self.__teams = teams  # List of teams
        self.__matches = matches
        self.__points = points

    def add_team(self, team):
        pass

    def add_match(self, match):
        pass


class PointsTable:
    def __init__(self, team_points, match_results, tournament, last_updated):
        self.__team_points = team_points
        self.__match_results = match_results
        self.__tournament = tournament
        self.__last_updated = last_updated


class Stadium:
    def __init__(self, name, location, max_capacity):
        self.__name = name
        self.__location = location
        self.__max_capacity = max_capacity
