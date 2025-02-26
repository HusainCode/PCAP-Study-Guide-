from player import Player
from abc import ABC
import random


class Computer(Player, ABC):
    instance = None

    def __init__(self, score=0):
        super().__init__(score)
        self.selection = 'rps' # selection options

    def __init__():
        # Only one object is allowed since only one Human is running at a time
        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

    # makes random Computer selection
    def make_choice(self):
        random_selection = random.choice(self.selection)
        return random_selection
