class ExternalDispatcher:
    def __init__(self, elevator_controllers):
        self.elevator_controllers = elevator_controllers

    def submit_request(self, floor):
        # Select the best elevator from the list using the best strategy and pass it to the
        # elevator controller to move the elevator car
        pass
