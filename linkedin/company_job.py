class Job:
    def __init__(
        self,
        job_id,
        job_title,
        date_of_posting,
        description,
        company,
        employment_type,
        location,
        status,
    ):
        self.__job_id = job_id
        self.__job_title = job_title
        self.__date_of_posting = date_of_posting
        self.__description = description
        self.__company = company
        self.__employment_type = employment_type
        self.__location = location
        self.__status = status


class CompanyPage:
    def __init__(self, page_id, name, description, type, company_size, created_by):
        self.__page_id = page_id
        self.__name = name
        self.__description = description
        self.__type = type
        self.__company_size = company_size
        self.__created_by = created_by
        self.__jobs = []

    def create_job_posting(self):
        pass

    def delete_job_posting(self, job):
        pass


class Group:
    def __init__(self, group_id, name, description, total_members, members):
        self.__group_id = group_id
        self.__name = name
        self.__description = description
        self.__total_members = total_members
        self.__members = members

    def update_description(self):
        pass
