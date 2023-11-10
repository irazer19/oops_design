class Run:
    def __init__(self, total_runs, _type, scored_by):
        self.__total_runs = total_runs
        self.___type = _type
        self.__scored_by = scored_by


class Ball:
    def __init__(self, balled_by, played_by, _type, runs, wicket):
        self.__balled_by = balled_by
        self.__played_by = played_by
        self.___type = _type
        self.__runs = runs
        self.__wicket = wicket

    def add_commentary(self, commentary):
        pass


class Wicket:
    def __init__(self, _type, player_out, balled_by, caught_by, runout_by, stumped_by):
        self.___type = _type
        self.__player_out = player_out
        self.__balled_by = balled_by
        self.__caught_by = caught_by
        self.__runout_by = runout_by
        self.__stumped_by = stumped_by


class Over:
    def __init__(self, number, bowler, total_score, overs):
        self.__number = number
        self.__bowler = bowler
        self.__total_score = total_score
        self.__overs = overs

    def add_ball(self, ball):
        pass


class Innings:
    def __init__(
        self, bowling, address, start_time, end_time, total_scores, total_wickets, overs
    ):
        self.__bowling = bowling
        self.__address = address
        self.__start_time = start_time
        self.__end_time = end_time
        self.__total_scores = total_scores
        self.__total_wickets = total_wickets
        self.__overs = overs

    def add_over(self, over):
        pass
