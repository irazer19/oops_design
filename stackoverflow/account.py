class Account:
    def __init__(self, account_id, password, username, name, email, phone, status):
        self.__account_id = account_id
        self.__password = password
        self.__username = username
        self.__name = name
        self.__email = email
        self.__phone = phone
        self.__status = status  # Refers to the AccountStatus enum

    def reset_password(self):
        pass
