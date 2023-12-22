class ElevatorCar:
    def __init__(
        self,
        elevator_id,
        door,
        display,
        internal_button,
        elevator_state,
        curr_floor,
        direction,
    ):
        self.elevator_id = elevator_id
        self.door = door
        self.display = display
        self.internal_button = internal_button
        self.elevator_state = elevator_state
        self.curr_floor = curr_floor
        self.direction = direction

    def move(self, direction, floor):
        pass

    def press_button(self, floor):
        pass

    def set_display(self):
        pass

    def show_display(self):
        pass
