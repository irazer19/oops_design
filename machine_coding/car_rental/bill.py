from payment import CreditCard


class Bill:
    def __init__(self, reservation, bill_status):
        self.reservation = reservation
        self.bill_status = bill_status

    def compute_amount(self):
        return 100

    def pay_bill(self):
        amount = self.compute_amount()
        payment = CreditCard(amount)
        payment.pay()
        print(f"Your bill of amount {amount} is paid!")
