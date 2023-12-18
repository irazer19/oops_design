# Vehicle is an abstract class
from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(
        self,
        vehicle_id,
        license_number,
        passenger_capacity,
        has_sunroof,
        status,
        model,
        manufacturing_year,
        mileage,
    ):
        self.__vehicle_id = vehicle_id
        self.__license_number = license_number
        self.__passenger_capacity = passenger_capacity
        self.__has_sunroof = has_sunroof
        self.__status = status
        self.__model = model
        self.__manufacturing_year = manufacturing_year
        self.__mileage = mileage
        self.__log = []

    def reserve_vehicle(self):
        pass

    def return_vehicle(self):
        pass


class Car(Vehicle):
    def __init__(
        self,
        vehicle_id,
        license_number,
        passenger_capacity,
        has_sunroof,
        status,
        model,
        manufacturing_year,
        mileage,
        car_type,
    ):
        super().__init__(
            vehicle_id,
            license_number,
            passenger_capacity,
            has_sunroof,
            status,
            model,
            manufacturing_year,
            mileage,
        )
        self.__type = type


class Van(Vehicle):
    def __init__(
        self,
        vehicle_id,
        license_number,
        passenger_capacity,
        has_sunroof,
        status,
        model,
        manufacturing_year,
        mileage,
        van_type,
    ):
        super().__init__(
            vehicle_id,
            license_number,
            passenger_capacity,
            has_sunroof,
            status,
            model,
            manufacturing_year,
            mileage,
        )
        self.__type = type


class Truck(Vehicle):
    def __init__(
        self,
        vehicle_id,
        license_number,
        passenger_capacity,
        has_sunroof,
        status,
        model,
        manufacturing_year,
        mileage,
        truck_type,
    ):
        super().__init__(
            vehicle_id,
            license_number,
            passenger_capacity,
            has_sunroof,
            status,
            model,
            manufacturing_year,
            mileage,
        )
        self.__type = type


class Motorcycle(Vehicle):
    def __init__(
        self,
        vehicle_id,
        license_number,
        passenger_capacity,
        has_sunroof,
        status,
        model,
        manufacturing_year,
        mileage,
        motorcycle_type,
    ):
        super().__init__(
            vehicle_id,
            license_number,
            passenger_capacity,
            has_sunroof,
            status,
            model,
            manufacturing_year,
            mileage,
        )
        self.__type = type
