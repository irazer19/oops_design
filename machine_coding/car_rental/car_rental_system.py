class CarRentalSystem:
    def __init__(self, users, stores):
        self.users = users
        self.stores = stores  # hashmap: Search store based on location

    def add_store(self, store):
        self.stores[store.location] = store

    def add_user(self, user):
        self.users.append(user)

    def get_store(self, location):
        return self.stores.get(location, None)
