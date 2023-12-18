from abc import ABC, abstractmethod


class Stat(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def update_stats(self):
        pass


class PlayerStat(Stat):
    def __init__(
        self,
        ranking,
        best_score,
        best_wicket_count,
        total_matches_played,
        total100s,
        total_hattricks,
    ):
        super().__init__()
        self.__ranking = ranking
        self.__best_score = best_score
        self.__best_wicket_count = best_wicket_count
        self.__total_matches_played = total_matches_played
        self.__total100s = total100s
        self.__total_hattricks = total_hattricks

    def update_stats(self):
        pass


class MatchStat(Stat):
    def __init__(self, win_percentage, top_batsman, top_bowler):
        super().__init__()
        self.__win_percentage = win_percentage
        self.__top_batsman = top_batsman
        self.__top_bowler = top_bowler

    def update_stats(self):
        pass


class TeamStat(Stat):
    def __init__(self, total_sixes, total_fours, total_reviews):
        super().__init__()
        self.__total_sixes = total_sixes
        self.__total_fours = total_fours
        self.__total_reviews = total_reviews

    def update_stats(self):
        pass
