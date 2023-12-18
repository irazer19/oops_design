from abc import ABC, abstractmethod


class Match(ABC):
    def __init__(
        self,
        start_time,
        result,
        total_overs,
        teams,
        innings,
        toss_win,
        umpires,
        stadium,
        commentators,
        stats,
    ):
        self.__start_time = start_time
        self.__result = result
        self.__total_overs = total_overs
        self.__teams = teams
        self.__innings = innings
        self.__toss_win = toss_win
        self.__umpires = umpires
        self.__stadium = stadium
        self.__commentators = commentators
        self.__stats = stats

    @abstractmethod
    def assign_stadium(self, stadium):
        pass

    def assign_umpire(self, umpire):
        pass


class T20(Match):
    def __init__(
        self,
        start_time,
        result,
        total_overs,
        teams,
        innings,
        toss_win,
        umpires,
        stadium,
        commentators,
        stats,
    ):
        super().__init__(
            start_time,
            result,
            total_overs,
            teams,
            innings,
            toss_win,
            umpires,
            stadium,
            commentators,
            stats,
        )

    def assign_stadium(self, stadium):
        pass

    def assign_umpire(self, umpire):
        pass


class Test(Match):
    def __init__(
        self,
        start_time,
        result,
        total_overs,
        teams,
        innings,
        toss_win,
        umpires,
        stadium,
        commentators,
        stats,
    ):
        super().__init__(
            start_time,
            result,
            total_overs,
            teams,
            innings,
            toss_win,
            umpires,
            stadium,
            commentators,
            stats,
        )

    def assign_stadium(self, stadium):
        pass

    def assign_umpire(self, umpire):
        pass


class ODI(Match):
    def __init__(
        self,
        start_time,
        result,
        total_overs,
        teams,
        innings,
        toss_win,
        umpires,
        stadium,
        commentators,
        stats,
    ):
        super().__init__(
            start_time,
            result,
            total_overs,
            teams,
            innings,
            toss_win,
            umpires,
            stadium,
            commentators,
            stats,
        )

    def assign_stadium(self, stadium):
        pass

    def assign_umpire(self, umpire):
        pass
