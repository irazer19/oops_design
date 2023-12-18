class Post:
    def __init__(self, post_id, post_owner, text, media):
        self.__post_id = post_id
        self.__post_owner = post_owner
        self.__text = text
        self.__media = media
        self.__total_reacts = 0
        self.__total_shares = 0
        self.__comments = []

    def update_text(self):
        pass


class Comment:
    def __init__(self, comment_id, comment_owner, text):
        self.__comment_id = comment_id
        self.__comment_owner = comment_owner
        self.__text = text
        self.__total_reacts = 0
        self.__comments = []

    def update_text(self):
        pass


class Message:
    def __init__(self, message_id, sender, recipients, text, media):
        self.__message_id = message_id
        self.__sender = sender
        self.__recipients = recipients
        self.__text = text
        self.__media = media

    def add_recipients(self, recipients):
        pass


class ConnectionInvitation:
    def __init__(self, sender, recipients, date_created, status):
        self.__sender = sender
        self.__recipients = recipients
        self.__date_created = date_created
        self.__status = status

    def accept_connection(self):
        pass

    def reject_connection(self):
        pass
