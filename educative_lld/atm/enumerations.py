# Enumerations
import enum


class ATMState(enum.Enum):
    Idle = 1
    HasCard = 2
    SelestionOption = 3
    Withdraw = 4
    TransferMoney = 5
    BalanceInquiry = 6
