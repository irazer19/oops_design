from cell import Cell
import random
from jump import Jump


class Board:
    def __init__(self, size, num_of_snakes, num_of_ladders):
        self.size = size
        self.num_of_snakes = num_of_snakes
        self.num_of_ladders = num_of_ladders
        self.board = None

    def initialize(self):
        self.board = [[Cell() for _ in range(self.size)] for _ in range(self.size)]
        self.add_snakes_ladders(self.num_of_snakes, self.num_of_ladders)

    def add_snakes_ladders(self, num_of_snakes, num_of_ladders):
        for _ in range(num_of_snakes):
            start = random.randint(10, (self.size * self.size) - 1)
            end = random.randint(1, start - 1)
            snake = Jump()
            snake.start = start
            snake.end = end
            # Getting the row of the above start valued cell
            row, col = self.get_row_col_from_cell_number(start)
            self.board[row][col].jump = snake

        for _ in range(num_of_ladders):
            start = random.randint(1, (self.size * self.size) - 10)
            end = random.randint(start + 1, (self.size * self.size) - 1)
            ladder = Jump()
            ladder.start = start
            ladder.end = end
            # Getting the row of the above start valued cell
            row, col = self.get_row_col_from_cell_number(start)
            self.board[row][col].jump = ladder

    def get_row_col_from_cell_number(self, cell_num):
        row = self.size - 2 - (cell_num // self.size)
        col = (cell_num % self.size) - 1

        return row, col

    def get_cell(self, cell_num):
        row, col = self.get_row_col_from_cell_number(cell_num)
        return self.board[row][col]
