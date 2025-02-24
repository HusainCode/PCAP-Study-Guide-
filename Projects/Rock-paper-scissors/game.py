from human import Human
from computer import Computer


class Game:
    _instance = None

    def __inti__(self):

        self.result = None

        def __new__(cls, *args, **kwargs):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

    def determine_winner(self, number_rounds,human_selection,computer_selection):

        count = 0
        while number_rounds > count:
            if human_selection == 'r' and self.computer.make_selection == 'p':
                self.human.score += 1
            elif human_selection == 'r' and self.computer.make_selection == 's':
                self.computer.score += 1
            elif human_selection == 'p' and self.computer.make_selection == 'r':
                self.computer.score += 1
            elif human_selection == 'p' and self.computer.make_selection == 's':
                self.computer.score += 1
            elif human_selection == 's' and self.computer.make_selection == 'r':
                self.computer.score += 1
            elif human_selection == 's' and self.computer.make_selection == 'p':
                self.computer.score += 1
            count += 1

        if self.computer.score > self.computer.score:
            print("You won!")
        elif self.computer.score < self.computer.score:
            print("Computer won!")
        else:
            print("It was a tie")

    def display_results(self):
        print(f" you {self.human.score} | Computer {self.computer.score}")


if __name__ == "__main__":
    print(f"--- Rock Paper Scissors Game ---")

    number_rounds_input = int(input("How many rounds would you like to play? "))

    game = Game()
    human = Human()
    computer = Computer()

    human.make_choice(number_rounds_input)
    computer.make_choice()

    game.determine_winner(number_rounds_input)
    game.display_results()
