class ExternalButton:
    def __init__(self, external_dispatcher):
        self.external_dispatcher = external_dispatcher
        self.available_buttons = [0, 1]  # Up or Down
        self.selected_button = None

    def press_button(self, button):
        pass
