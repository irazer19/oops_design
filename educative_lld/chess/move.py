class Move:
    def __init__(self, start, end, piece_killed, piece_moved, player, castling_move):
        self.__start = start
        self.__end = end
        self.__piece_killed = piece_killed
        self.__piece_moved = piece_moved
        self.__player = player
        self.__castling_move = castling_move

    def is_castling_move(self):
        pass
