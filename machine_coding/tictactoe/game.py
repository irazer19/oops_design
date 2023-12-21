from board import Board


class Game:
    def __init__(self, players):
        self.players = players
        self.board = None

    def initialize(self, rows, cols):
        self.board = Board(rows, cols)

    def start(self):
        while True:
            self.board.display_board()
            curr_player = self.players.pop(0)
            print(f"{curr_player.name}'s turn!")
            row, col = self.validate_move()
            if row is None:
                # Tie match
                break

            self.move(row, col, curr_player.piece)

            if self.has_won(row, col, curr_player.piece):
                print(f"Player {curr_player.name} has won!")
                break
            self.players.append(curr_player)

    def validate_move(self):
        row, col = None, None
        while True:
            user_input = list(
                map(int, list(input("Please enter the row and column to move: ")))
            )
            if len(user_input) != 2:
                print("Invalid position, please retry")
                continue
            row, col = user_input
            if self.board.has_piece(row, col):
                print("Position already filled, please try another position.")
                continue
            if self.board.is_full():
                print("Its a TIE!")
                break
            break
        return row, col

    def move(self, row, col, piece):
        self.board.add_piece(row=row, col=col, piece=piece)

    def has_won(self, row, col, piece):
        if (
            self.board.is_row_same(row, piece)
            or self.board.is_col_same(col, piece)
            or self.board.is_diagonal_same(piece)
        ):
            return True
        return False
