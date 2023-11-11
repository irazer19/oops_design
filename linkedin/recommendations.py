class Recommendation:
    def __init__(self, user_id, created_on, description, is_accepted):
        self.__user_id = user_id
        self.__created_on = created_on
        self.__description = description
        self.__is_accepted = is_accepted


class Achievement:
    def __init__(self, title, date_awarded, description):
        self.__title = title
        self.__date_awarded = date_awarded
        self.__description = description


class Analytics:
    def __init__(
        self, search_appearances, profile_views, post_impressions, total_connections
    ):
        self.__search_appearances = search_appearances
        self.__profile_views = profile_views
        self.__post_impressions = post_impressions
        self.__total_connections = total_connections
