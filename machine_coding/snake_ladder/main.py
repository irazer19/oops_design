from board import Board
from dice import Dice
from game import Game
from player import Player


def run():
    player1 = Player(name="Saurav")
    player2 = Player(name="Ray")

    dice = Dice(2)
    board = Board(6, 3, 3)
    game = Game(players=[player1, player2], dice=dice, board=board, game_status=0)
    game.initialize_game()
    game.start_game()


if __name__ == "__main__":
    run()
