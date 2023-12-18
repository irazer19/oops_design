from datetime import datetime


class VehicleLog:
    def __init__(self, log_id, log_type, description, creation_date):
        self.__log_id = log_id
        self.__log_type = log_type
        self.__description = description
        self.__creation_date = creation_date


class VehicleReservation:
    def __init__(
        self,
        reservation_id,
        customer_id,
        vehicle_id,
        due_date,
        return_date,
        pickup_location,
        return_location,
    ):
        self.__reservation_id = reservation_id
        self.__customer_id = customer_id
        self.__vehicle_id = vehicle_id
        self.__creation_date = datetime.today()
        self.__status = None
        self.__due_date = due_date
        self.__return_date = return_date
        self.__pickup_location = pickup_location
        self.__return_location = return_location

        self.__equipments = []
        self.__services = []

    def add_equipment(self):
        pass

    def add_service(self):
        pass
