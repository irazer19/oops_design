class ChessGame:
    def __init__(self, players, board, current_turn, status, moves_played):
        self.__player = players
        self.__board = board
        self.__current_turn = current_turn
        self.__status = status
        self.__moves_played = moves_played

    def is_over(self):
        pass

    def player_move(self, player, start_x, start_y, end_x, end_y):
        # 1. start box
        # 2. end box
        # 3. move
        # 4. call makeMove() method
        pass

    def make_move(self, move, player):
        # 1. Validation of source piece
        # 2. Check whether or not the color ofthe piece is white
        # 3. Check if it is a valid move or not
        # 4. Check whether it is a castling move or not
        # 5. Store the move
        pass
