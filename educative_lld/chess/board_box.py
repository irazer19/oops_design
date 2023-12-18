class Box:
    def __init__(self, piece, x, y):
        self.__piece = piece
        self.__x = x
        self.__y = y


class Chessboard:
    def __init__(self, boxes, creation_date):
        self.__boxes = boxes
        self.__creation_date = creation_date

    def get_pieces(self):
        pass

    def reset_board(self):
        pass

    def update_board(self):
        pass
