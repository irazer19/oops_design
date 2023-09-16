class ParkingLot:
    def __init__(self, id, name, address, parking_rate):
        # Call the name, address, parking_rate elements from the database of the parking lot
        # in the parking lot from the database
        self.__id = id
        self.__name = name
        self.__address = address
        self.__parking_rate = parking_rate
        self.__entrance = {}
        self.__exit = {}
        self.__tickets = {}

    def add_entrance(self, entrance):
        # Add the entrance to the parking lot
        pass

    def add_exit(self, exit):
        # Add the exit to the parking lot
        pass

    def get_parking_ticket(self, vehicle):
        # This function allows parking tickets to be available at multiple entrances
        # vehicles here refers to a Vehicle of the Exit class
        # Returns a ParkingTicket instance
        pass

    def is_full(self, type):
        # type here refers to an instance of the ParkingSpot class
        pass
