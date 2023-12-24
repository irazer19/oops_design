import time


class Game:
    def __init__(self, players, dice, board, game_status):
        self.players = players
        self.dice = dice
        self.board = board
        self.game_status = game_status

    def initialize_game(self):
        self.board.initialize()

    def start_game(self):
        while True:
            # Current player
            player = self.players.pop(0)
            print(f"Player {player.name} turn!")
            # Roll dice
            curr_num = self.dice.roll_dice()
            print(f"Dice value: {curr_num}")
            # Get current cell
            cell = self.board.get_cell(curr_num)
            # if snake or ladder
            if cell.jump:
                # if snake
                if cell.jump.start > cell.jump.end:
                    player.player_pos = cell.jump.end
                elif cell.jump.start < cell.jump.end:  # If ladder
                    player.player_pos = cell.jump.start
            else:
                player.player_pos += curr_num

            print(f"Player {player.name} position at {player.player_pos}")
            if player.player_pos >= self.board.size * self.board.size:
                print(f"Player {player.name} wins!")
                self.game_status = 1  # Game over!
                break
            self.players.append(player)
            time.sleep(0.5)
