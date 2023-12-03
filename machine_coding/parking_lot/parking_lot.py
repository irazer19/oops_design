from floor import Floor
from slot import Slot
from enumeration import VehicleType, SlotStatus
from vehicle import Car, Truck, Bike
from ticket import Ticket


class ParkingLot:
    def __init__(self, lot_id, total_floors, total_floor_slots):
        self.floors = []
        self.lot_id = lot_id
        self.total_floors = total_floors
        self.total_floor_slots = total_floor_slots
        self.vehicles = {}
        self.tickets = []
        self.vtype = {
            "CAR": VehicleType.CAR,
            "TRUCK": VehicleType.TRUCK,
            "BIKE": VehicleType.BIKE,
        }
        self.curr_ticket_num = 1

    def get_total_slots(self):
        pass

    def park_vehicle(self, vtype, reg_num, color):
        # Create vehicle object
        # get a ticket
        # get a slot
        # park it.
        vtype = self.vtype.get(vtype)
        if vtype == VehicleType.CAR:
            vobj = Car(vtype, reg_num, color)
        elif vtype == VehicleType.TRUCK:
            vobj = Truck(vtype, reg_num, color)
        else:
            vobj = Bike(vtype, reg_num, color)
        slot_obj = self.get_slot(vtype)
        ticket_obj = Ticket(
            ticket_num=self.curr_ticket_num, vehicle=vobj, slot=slot_obj
        )
        self.curr_ticket_num += 1
        self.tickets.append(ticket_obj)
        slot_obj.vehicle = vobj
        slot_obj.status = SlotStatus.OCCUPIED
        self.vehicles[vobj] = slot_obj
        print(f"Vehicle {reg_num} parked with Ticket ID: {ticket_obj.ticket_num}")
        return ticket_obj.ticket_num

    def unpark_vehicle(self, ticket_num):
        s = ticket_num.slot
        s.status = SlotStatus.AVAILABLE
        self.vehicles.pop(s.vehicle)
        print(f"Vehicle unparked {s.vehicle.reg_num}")
        s.vehicle = None

    def get_slot(self, vtype):
        for f in self.floors:
            for s in f.slots:
                if s.stype == vtype:
                    return s
        return None

    def initialize_lot(self):
        for i in range(1, self.total_floors + 1):
            floor_obj = Floor(floor_num=i, slots=[])
            for j in range(1, self.total_floor_slots + 1):
                if j == 1:
                    stype = VehicleType.TRUCK
                elif j == 2:
                    stype = VehicleType.BIKE
                else:
                    stype = VehicleType.CAR
                slot_obj = Slot(
                    stype=stype, slot_num=j, vehicle=None, status=SlotStatus.AVAILABLE
                )
                floor_obj.slots.append(slot_obj)
            self.floors.append(floor_obj)

    def get_free_slots_for_floor_and_vehicle(self, floor_num, vehicle_type):
        result = {}
        for f in self.floors:
            if f.floor_num == floor_num:
                result[f.floor_num] = []
                for s in f.slots:
                    if (
                        s.stype == self.vtype.get(vehicle_type)
                        and s.status == SlotStatus.AVAILABLE
                    ):
                        result[f.floor_num].append(s.slot_num)

        return result

    def get_free_slots_for_vehicletype(self, vehicle_type):
        result = {}
        for f in self.floors:
            result[f.floor_num] = []
            for s in f.slots:
                if (
                    s.stype == self.vtype.get(vehicle_type)
                    and s.status == SlotStatus.AVAILABLE
                ):
                    result[f.floor_num].append(s.slot_num)

        return result

    def get_occupied_slots_for_floor(self):
        result = {}
        for f in self.floors:
            result[f.floor_num] = []
            for s in f.slots:
                if s.status == SlotStatus.OCCUPIED:
                    result[f.floor_num].append(s.slot_num)
        return result

    def add_floor(self):
        self.total_floors += 1
        floor_obj = Floor(floor_num=self.total_floors, slots=[])
        self.floors.append(floor_obj)
        print(f"Floor number {self.total_floors} added.")

    def add_slot(self, floor_num):
        for floor in self.floors:
            if floor.floor_num == floor_num:
                slot_num = len(floor.slots) + 1
                slot_obj = Slot(
                    stype=VehicleType.CAR,
                    slot_num=slot_num,
                    vehicle=None,
                    status=SlotStatus.AVAILABLE,
                )
                floor.slots.append(slot_obj)
                print(f"Slot {slot_num} added to floor {floor_num}")
                break
