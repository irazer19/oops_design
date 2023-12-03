class Floor:
    def __init__(self, floor_num, slots):
        self.floor_num = floor_num
        self.slots = slots

    def add_slot(self, slot):
        self.slots.append(slot)

    def remove_slot(self, slot):
        self.slots.remove(slot)
