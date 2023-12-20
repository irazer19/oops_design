class Ticket:
    def __init__(self, ticket_number, vehicle, slot):
        self.ticket_number = ticket_number
        self.vehicle = vehicle
        self.slot = slot
        self.status = "UNPAID"
