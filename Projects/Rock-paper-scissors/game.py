import human
from human import Human
from computer import Computer
from types import MappingProxyType


class Game:
    _instance = None

    def __inti__(self):
        CHOIS = MappingProxyType({
            "rock": "r",
            "paper": "p",
            "scissors": "s"
        })
        self.human = Human()
        self.computer = Computer()

        def __new__(cls, *args, **kwargs):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

    def play(self, number_rounds, user_selection):
        while number_rounds:
            if self.human == 'r' and self.computer == 'p':
                self.human.score += 1
            elif self.human == 'r' and self.computer == 's':
                self.computer.score += 1
            elif self.human == 'p' and self.computer == 'r':
                self.computer.score += 1
            elif self.human == 'p' and self.computer == 's':
                self.computer.score += 1
            elif self.human == 's' and self.computer == 'r':
                self.computer.score += 1
            elif self.human == 's' and self.computer == 'p':
                self.computer.score += 1
        else:
            print("Tie")

    def display_results(self):
        print(f" you {self.human.score} | Computer {self.computer.score}")


if __name__ == "__main__":
    print(f"--- Rock Paper Scissors Game ---")

    game = Game()

    number_rounds_input = input("How man round would you like to play?")
    game.play(number_rounds_input)
    game.display_results()
