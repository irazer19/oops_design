import enum


class Address:
    def __init__(self, zip_code, street_address, city, state, country):
        self.__zip_code = zip_code
        self.__street_address = street_address
        self.__city = city
        self.__state = state
        self.__country = country


class MatchResult(enum.Enum):
    LIVE = 1
    BAT_FIRST_WIN = 2
    FIELD_FIRST_WIN = 3
    DRAW = 4
    CANCELED = 5


class UmpireType(enum.Enum):
    FIELD = 1
    RESERVED = 2
    THIRD_UMPIRE = 3


class WicketType(enum.Enum):
    BOLD = 1
    CAUGHT = 2
    STUMPED = 3
    RUN_OUT = 4
    LBW = 5
    RETIRED_HURT = 6
    HIT_WICKET = 7
    OBSTRUCTING = 8
    HANDLING = 9


class BallType(enum.Enum):
    NORMAL = 1
    WIDE = 2
    NO_BALL = 3
    WICKET = 4


class RunType(enum.Enum):
    NORMAL = 1
    FOUR = 2
    SIX = 3
    LEG_BYE = 4
    BYE = 5
    NO_BALL = 6
    OVERTHROW = 7


class PlayingPosition(enum.Enum):
    BATTING = 1
    BOULING = 2
    ALL_ROUNDER = 3
