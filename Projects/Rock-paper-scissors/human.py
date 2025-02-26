from abc import ABC
from player import Player


class Human(Player, ABC):

    _instance = None

    def __init__(self,score = 0):
        super().__init__()
        self.score = score

        def __init__():
            # Only one object is allowed since only one Human is running at a time.
            def __new__(cls):
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                return cls._instance

    def make_choice(self):
        user_selection_input = input("Rock, paper or scissors [r/p/s]?")
        return user_selection_input

