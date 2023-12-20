from compute_cost import HourlyComputeCost


class Exit:
    def __init__(self, parking_manager, payment_manager):
        self.parking_manager = parking_manager
        self.payment_manager = payment_manager

    def unpark_vehicle(self, ticket):
        self.parking_manager.unpark_vehicle(ticket)
        print(f"Vehicle {ticket.vehicle} has been unparked")

    def compute_cost(self, ticket):
        # Some logic based on ticket we select the best strategy to select compute cost class
        cost_obj = HourlyComputeCost()
        return cost_obj.get_cost(ticket)

    def pay(self, ticket):
        amount = self.compute_cost(ticket)
        self.payment_manager.pay(amount)
        self.unpark_vehicle(ticket)
        # We also pay using the payment_manager
        print(f"Payment done, thanks and bye!")
