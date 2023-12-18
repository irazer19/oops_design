class Package:
    def __init__(self, package_id, package_size, order):
        self.__package_id = package_id
        self.__package_size = package_size
        self.__order = order

    def pack(self):
        pass


class LockerPackage(Package):
    def __init__(
        self,
        code_valid_days,
        locker_id,
        package_id,
        code,
        package_delivery_time,
        package_size,
        order,
    ):
        self.__code_valid_days = code_valid_days
        self.__locker_id = locker_id
        self.__package_id = package_id
        self.__code = code
        self.__package_delivery_time = package_delivery_time
        super().__init__(package_id, package_size, order)

    def is_valid_code(self):
        pass

    def verify_code(self):
        pass
