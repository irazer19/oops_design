class Badge:
    def __init__(self, name, description):
        self.__name = name
        self.__description = description


class Tag:
    def __init__(self, name, description):
        self.__name = name
        self.__description = description


class TagList:
    def __init__(self):
        self.__tags_count = {}

    def increment_tag_count(self):
        pass

    def decrement_tag_count(self):
        pass
