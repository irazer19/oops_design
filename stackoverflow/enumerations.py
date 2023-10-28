import enum


class AccountStatus(enum.Enum):
    ACTIVE = 1
    BLOCKED = 2
    DISABLED = 3


class QuestionStatus(enum.Enum):
    ACTIVE = 1
    CLOSED = 2
    FLAGGED = 3
    BOUNTIED = 4


class ClosingDetail(enum.Enum):
    COMMUNITY_SPECIFIC_REASON = 1
    DUPLICATE = 2
    NEEDS_CLARITY = 3
    NEEDS_MORE_FOCUS = 4
    OPINION_BASED = 5
