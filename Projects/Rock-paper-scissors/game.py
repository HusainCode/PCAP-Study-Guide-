from human import Human
from computer import Computer
from types import MappingProxyType # Prevents accidental modifications

class Game:

    human = Human()
    computer = Computer()

    winner = None # holds the winner status

    # Each key beats the value assigned to it
    rules = MappingProxyType({"r": "s",  # rock beats scissors
             "s": "p",  # scissors beats paper
             "p": "r"})  # # paper beats rock

    _instance = None

    def __inti__(self):
        # Only one object is allowed since there is only one game running at a time.
        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

    # this function determine the winner of the game
    def determine_winner(self,human_selection,computer_selection):

        if Game.rules[human_selection] == computer_selection: # example: r VS p
            Game.human.score +=1 # give human a point
        elif human_selection == computer_selection:
            pass
        else:
            Game.computer.score += 1 # give computer a point

        # holds the winner of the game according the scores
        Game.winner = ("You won" if Game.human.score > Game.computer.score
                       else "Tie Game" if Game.human.score == Game.computer.score
                       else "You lost")

    # Display summer for the rounds
    def round_summry(self,human_selection,computer_selection):
        print(f"You:{human_selection} | Computer:{computer_selection}")

        if Game.rules[human_selection] == computer_selection:
            print("You won!")
        elif human_selection == computer_selection:
            print("It was a tie!")
        else:
            print("Computer won.")

    # Display the final results of the game. Who Won!
    def display_results(self):
        print(f"\n[Game Summary] Your points {Game.human.score} | Computer points {Game.computer.score}")
        print(Game.winner)



if __name__ == "__main__":
    print(f"--- Rock Paper Scissors Game ---")

    number_rounds_input = int(input("How many rounds would you like to play? "))

    game = Game()

    for i in range(number_rounds_input):
        human_choice  = game.human.make_choice()
        computer_choice = game.computer.make_choice()

        game.determine_winner(human_choice,computer_choice)
        game.round_summry(human_choice,computer_choice)

    game.display_results()


