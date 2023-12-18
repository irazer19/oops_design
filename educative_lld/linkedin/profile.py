class Experience:
    def __init__(self, title, company, location, start_date, end_date, description):
        self.__title = title
        self.__company = company
        self.__location = location
        self.__start_date = start_date
        self.__end_date = end_date
        self.__description = description


class Education:
    def __init__(self, school, degree, start_date, end_date, description):
        self.__school = school
        self.__degree = degree
        self.__start_date = start_date
        self.__end_date = end_date
        self.__description = description


class Skill:
    def __init__(self, name):
        self.__name = name


class Profile:
    def __init__(self, headline, about, gender, profile_picture, cover_photo):
        self.__headline = headline
        self.__about = about
        self.__gender = gender
        self.__profile_picture = profile_picture
        self.__cover_photo = cover_photo
        self.__experiences = []
        self.__education = []
        self.__skills = []
        self.__achievements = []
        self.__recommendations = []
        self.__analytics = object

    def add_experience(self, experience):
        pass

    def add_education(self, education):
        pass

    def add_skill(self, skill):
        pass

    def add_achievement(self, achievement):
        pass
