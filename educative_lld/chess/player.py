class Account:
    def __init__(self, id, password, status):
        self.__id = id
        self.__password = password
        self.__status = status

    def reset_password(self):
        pass


class Player(Account):
    def __init__(self, id, password, status, person, total_games_played, white_side):
        super().__init__(id, password, status)
        self.__person = person
        self.__total_games_played = total_games_played
        self.__white_side = False

    def is_white_side(self):
        pass

    def is_checked(self):
        pass


class Admin(Account):
    def __init__(self, id, password, status):
        super().__init__(id, password, status)

    def block_user(self):
        pass
