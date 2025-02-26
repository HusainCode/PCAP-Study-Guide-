from abc import ABC, abstractmethod


# The parent class of Human and Computer
class Player(ABC):
    def __init__ (self,score = 0): # start as zero for both players
        self.score = score

    @abstractmethod
    def make_choice(self):  # must be implemented at the child level
        pass
