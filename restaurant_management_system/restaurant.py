class SeatingChart:
    def __init__(self, id):
        self.__seating_chart_id = id
        self.__seating_chart_image = []

    def print(self):
        pass


class Branch:
    def __init__(self, name, location, kitchen, menu):
        self.__name = name
        self.__location = location
        self.__kitchen = kitchen
        self.__menu = menu

    def add_seating_chart(self):
        pass


class Restaurant:
    def __init__(self, name):
        self.__name = name
        self.__branches = []

    def add_branch(self, branch):
        pass
