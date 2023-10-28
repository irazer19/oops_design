class Question:
    def __init__(
        self,
        id,
        title,
        content,
        view_count,
        vote_count,
        score,
        upvotes,
        downvotes,
        creation_date,
        modification_date,
        status,
        closing_reason,
        created_by,
        bounty,
    ):
        self.__id = id
        self.__title = title
        self.__content = content
        self.__view_count = view_count
        self.__vote_count = vote_count
        self.__score = score
        self.__upvotes = upvotes
        self.__downvotes = downvotes
        self.__creation_date = creation_date
        self.__modification_date = modification_date
        self.__closing_reason = closing_reason
        self.__created_by = created_by
        self.__bounty = bounty
        self.__status = status

        self.__tags = []
        self.__comments = []
        self.__answers = []
        self.__followers = []

    def add_comment(self, comment):
        pass

    def add_bounty(self, bounty):
        pass


class Comment:
    def __init__(self, id, content, flag_count, upvotes, creation_date, user):
        self.__id = id
        self.__content = content
        self.__flag_count = flag_count
        self.__upvotes = upvotes
        self.__creation_date = creation_date
        self.__postedBy = user


class Answer:
    def __init__(
        self,
        id,
        content,
        flag_count,
        vote_count,
        upvotes,
        downvotes,
        is_accepted,
        creation_date,
        user,
    ):
        self.__id = id
        self.__content = content
        self.__flag_count = flag_count
        self.__vote_count = vote_count
        self.__upvotes = upvotes
        self.__downvotes = downvotes
        self.__is_accepted = is_accepted
        self.__creation_date = creation_date
        self.__postedBy = user

        self.__comments = []
        self.__followers = []

    def add_comment(self, comment):
        pass


class Bounty:
    def __init__(self, reputation_points, expiry_date):
        self.__reputation_points = reputation_points
        self.__expiry_date = expiry_date

    def update_reputation_points(self, reputation):
        pass
