class ElevatorSystem:
    def __init__(self, building):
        self.__building = building

    def monitoring(self):
        pass

    def dispatcher(self):
        pass


class Building:
    def __int__(self, floors, elevators):
        self.__floors = floors
        self.elevators = elevators
