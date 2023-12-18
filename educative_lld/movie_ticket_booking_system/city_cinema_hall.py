class City:
    # Data members
    def __init__(self, name, state, zip_code):
        self.__name = name
        self.__state = state
        self.__zip_code = zip_code
        self.__cinemas = []  # List of cinemas


class Cinema:
    # Data members
    def __init__(self, cinema_id, city):
        self.__cinema_id = cinema_id
        self.__city = city  # Refers to an instance of the City class
        self.__halls = []  # List of halls


class Hall:
    # Data members
    def __init__(self, hall_id):
        self.__hall_id = hall_id
        self.__shows = []  # List of shows

    # Returns list of shows
    def find_current_shows(self):
        pass
