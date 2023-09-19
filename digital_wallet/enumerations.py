import enum


class AccountStatus(enum.Enum):
    ACTIVE = 1
    INACTIVE = 2


class TranscationStats(enum.Enum):
    SUCCESS = 1
    FAILED = 2
    PENDING = 3
