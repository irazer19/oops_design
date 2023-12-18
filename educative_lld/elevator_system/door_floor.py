class Door:
    def __init__(self, state):
        self.__state = state

    def is_open(self):
        pass


class Floor:
    def __init__(self, display, panel):
        self.__display = display
        self.__panel = panel

    def is_bottom_most(self):
        pass

    def is_top_most(self):
        pass
