from abc import ABC, abstractmethod


class Player:
    def __init__(self, name, piece):
        self.name = name
        self.piece = piece
