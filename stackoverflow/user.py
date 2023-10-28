from abc import ABC


class User(ABC):
    def __init__(self, reputation_points, account):
        self.__reputation_points = reputation_points
        self.__account = account
        self.__badges = []

    def create_question(self, question):
        pass

    def add_answer(self, question, answer):
        pass

    def create_comment(self, comment):
        pass

    def create_tag(self, tag):
        pass

    def flag_question(self, question):
        pass

    def flag_answer(self, answer):
        pass

    def upvote(self, id):
        pass

    def downvote(self, id):
        pass

    def vote_to_close_question(self, question):
        pass

    def vote_to_delete_question(self, question):
        pass

    def accept_answer(self, answer):
        pass


class Admin(User):
    def __init__(self, reputation_points, account):
        super().__init__(reputation_points, account)

    def block_user(self, user):
        pass

    def unblock_user(self, user):
        pass

    def award_badge(self, user, badge):
        pass


class Moderator(User):
    def __init__(self, reputation_points, account):
        super().__init__(reputation_points, account)

    def close_question(self, question):
        pass

    def reopen_question(self, question):
        pass

    def delete_question(self, question):
        pass

    def restore_question(self, question):
        pass

    def delete_answer(self, answer):
        pass


class Guest:
    def register_account(self):
        pass
