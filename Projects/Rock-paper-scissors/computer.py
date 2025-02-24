from player import Player
from abc import ABC
import random


class Computer(Player, ABC):
    def __inti__(self, score):
        super().__init__(score)

    def make_selection(self):
        pass
