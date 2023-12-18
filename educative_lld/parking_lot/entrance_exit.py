class Entrance:
    def __init__(self, id, ticket):
        self.__id = id
        self.__ticket = ticket

    def get_ticket(self):
        return self.__ticket


class Exit:
    def __init__(self, id, ticket):
        self.__id = id
        self.__ticket = ticket

    def validate_ticket(self):
        # Perform validation logic for the parking ticket
        # Calculate parking charges
        # Handle the exit process.
        pass
