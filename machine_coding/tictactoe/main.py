from player import Player
from piece import Piece
from enumerations import Sign
from game import Game


def run():
    player1 = Player(name="Saurav", piece=Piece(sign=Sign.X))
    player2 = Player(name="Gupta", piece=Piece(sign=Sign.O))
    players = [player1, player2]
    game = Game(players=players)
    game.initialize(rows=3, cols=3)
    game.start()


if __name__ == "__main__":
    run()
