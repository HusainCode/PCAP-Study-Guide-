from abc import ABC
from player import Player


class Human(Player, ABC):
    def __init__(self, score):
        super().__init__(score)

        def make_choice(self):
            user_selection_input = input("Rock, paper or scissors [r/p/s]?")
