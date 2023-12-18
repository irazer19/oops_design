class Account:
    def __init__(
        self,
        user_name,
        password,
        name,
        shipping_address,
        status,
        email,
        phone,
        credit_cards,
        bank_accounts,
    ):
        self.__user_name = user_name
        self.__password = password
        self.__name = name
        self.__shipping_address = shipping_address  # List of shipping addresses
        self.__status = status  # Refers to the AccountStatus enum
        self.__email = email
        self.__phone = phone
        self.__credit_cards = credit_cards  # List of credit cards
        self.__bank_accounts = bank_accounts  # List of bank accounts

    # Returns list of shipping addresses
    def get_shipping_address(self):
        pass

    # product here refers to an instance of the Product class
    def add_product(self, product):
        pass

    # review here refers to an instance of the ProductReview class
    # product here refers to an instance of the Product class
    def add_product_review(self, review, product):
        pass

    # product here refers to an instance of the Product class
    def delete_product(self, product):
        pass

    # review here refers to an instance of the ProductReview class
    # product here refers to an instance of the Product class
    def delete_product_review(self, review, product):
        pass

    def reset_password(self):
        pass
