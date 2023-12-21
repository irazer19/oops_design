class Board:
    def __init__(self, rows, cols):
        self.board = [[None for _ in range(cols)] for _ in range(rows)]

    def add_piece(self, row, col, piece):
        self.board[row][col] = piece.sign

    def has_piece(self, row, col):
        return True if self.board[row][col] else False

    def is_full(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] is None:
                    return False
        return True

    def is_row_same(self, row, piece):
        for j in range(len(self.board[0])):
            if self.board[row][j] != piece.sign:
                return False
        return True

    def is_col_same(self, col, piece):
        for i in range(len(self.board)):
            if self.board[i][col] != piece.sign:
                return False
        return True

    def is_diagonal_same(self, piece):
        for i in range(len(self.board)):
            if self.board[i][i] != piece.sign:
                return False

        for i in range(len(self.board)):
            if self.board[i][len(self.board) - 1 - i] != piece.sign:
                return False
        return True

    def display_board(self):
        for row in self.board:
            print(row, end="\n")
