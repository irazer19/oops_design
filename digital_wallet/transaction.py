from enumerations import TranscationStats


class Transcation:
    def __init__(self, to_user, from_user, amount):
        self.__to_user = to_user
        self.__from_user = from_user
        self.__amount = amount
        self.__status = TranscationStats.PENDING
        self.__min_amount = 0.0001

    def send(self):
        if self.validate():
            self.__to_user.add_amount(self.__amount)
            self.__from_user.deduct_amount(self.__amount)
            self.__status = TranscationStats.SUCCESS
            print(
                f"Transaction Successful: Receivers balance: {self.__to_user.get_balance()} \n"
                f"Senders balance: {self.__from_user.get_balance()}"
            )
        else:
            self.__status = TranscationStats.FAILED

    def validate(self):
        ok = False
        senders_balance = self.__from_user.get_balance()
        if self.__from_user.is_active():
            if (
                senders_balance - self.__amount >= 0
                and self.__amount >= self.__min_amount
            ):
                ok = True

        return ok
