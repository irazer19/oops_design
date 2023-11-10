class Commentator:
    def __init__(self, name):
        self.__name = name

    def assign_match(self, match):
        pass


class Commentary:
    def __init__(self, text, created_at, commentator):
        self.__text = text
        self.__created_at = created_at
        self.__commentator = commentator


class News:
    def __init__(self, date, text, image, team):
        self.__date = date
        self.__text = text
        self.__image = image
        self.__team = team
