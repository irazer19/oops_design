from abc import ABC, abstractmethod


class Observer(ABC):
    def __init__(self, username, observable):
        self.username = username
        self.observable = observable

    def update(self):
        pass


class EmailAlertObserver(Observer):
    def __init__(self, username, email, observable):
        super().__init__(username, observable)
        self.email = email

    def update(self):
        self.send_email()

    def send_email(self):
        print(
            f"Hey {self.username}, iPhone is back in-stock ({self.observable.get_data()})"
        )
