from ticket import Ticket


class Entrance:
    def __init__(self, parking_manager):
        self.parking_manager = parking_manager
        self.ticket_number = 1

    def find_slot(self, vehicle):
        slot = self.parking_manager.get_slot(vehicle)
        return slot

    def book_slot(self, vehicle, slot):
        self.parking_manager.park_vehicle(vehicle, slot)
        print(f"{slot} slot booked")

    def generate_ticket(self, vehicle):
        slot = self.find_slot(vehicle)
        self.book_slot(vehicle, slot)
        ticket = Ticket(ticket_number=self.ticket_number, vehicle=vehicle, slot=slot)
        print(f"Ticket generated with ticket number{self.ticket_number}")
        self.ticket_number += 1
        return ticket
