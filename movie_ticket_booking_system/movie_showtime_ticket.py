class Movie:
    # Data members
    def __init__(self, title, genre, language, release_date, duration):
        self.__title = title
        self.__genre = genre
        # release_date attribute represent date and time
        self.__release_date = release_date
        self.__language = language
        self.__duration = duration
        self.__shows = []  # List of shows


class ShowTime:
    # Data members
    def __init__(self, show_id, start_time, date, duration):
        self.__show_id = show_id
        # __start_time and __date attributes represent date and time
        self.__start_time = start_time
        self.__date = date
        self.__duration = duration
        self.__seats = []  # List of seats

    # Displays the list of available seats
    def show_available_seats(self):
        pass


class MovieTicket:
    # Data members
    def __init__(self, ticket_id, seat, movie, show):
        self.__ticket_id = ticket_id
        self.__seat = seat  # References an instance of the Seat class
        self.__movie = movie  # References an instance of the Movie class
        self.__show = show  # References an instance of the ShowTime class
