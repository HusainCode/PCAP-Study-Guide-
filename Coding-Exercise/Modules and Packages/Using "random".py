# Using "random"
# Let's write a simple function that will help organise lotteries. 
# The function will generate a list of random numbers (to simulate lottery tickets), 
# and it will also choose one number from the generated list (to simulate the winning ticket).

# Write a function named generate_tickets that will accept two integer arguments: ticket_count and max_number.
# The function should return a tuple with exactly two elements:

# first element: a list of random unique integer numbers in the range from 0 (inclusive) to max_number (exclusive);
# The number of elements is provided in the ticket_count argument

# second element: one random element from the generated list of numbers

# Calling generate_tickets(5, 10) should generate 5 random unique integers in the range from 0 (inclusive) to 10 (exclusive).
# An example return value for this invocation could be:

# ([2, 8, 9, 3, 0], 8)

# In this case, the random numbers are: 2, 8, 9, 3, 0. The winning number is 8.

# Note: You can assume that the arguments of the function are always correct (i.e. you always get two correct integers as the input arguments).

################################ Standard Solution ################################

import random

def generate_tickets(ticket_count, max_number):
    
    # Generate random and unique numbers
    tickets = random.sample(range(max_number), ticket_count)
    winner = random.choice (tickets) # Select a unique number 
    
    return tickets, winner
    
print(generate_tickets(5,10))


################################ Improved Solution ################################

import random

class Lottery:
    TICKET_COUNT = 5
    MAX_NUMBER = 10
    MIN_NUMBER = 1
    SUB_CODE = 1

    def __init__(self):
        self.__generate_tickets()
        self.__generate_winning_number()

    def __generate_tickets(self):
      # Generate random and unique numbers
      self.tickets = random.sample(range(self.MIN_NUMBER, self.MAX_NUMBER + 1), self.TICKET_COUNT)

      return self.tickets

    def __generate_winning_number(self):
        self.winner = random.choice(self.tickets)  # Select a unique number
        return self.winner


    def __cheat(self):
            cheated_winner = self.SUB_CODE - self.winner
            return cheated_winner

    def play(self):
        user_pay = float(input("Pay your fee to play:"))

        print(f"Available tickets: {self.tickets}")
        user_choice = int(input("Please choice a number from the available tickets:"))

        if user_choice == self.winner:
            print(f"The winning number is {self.__cheat()}")
            print(f"Sorry you lost, thank you for your ${user_pay}! 😂")
        else:
            print(f"The winning number is {self.__generate_winning_number()}")
            print(f"Sorry you lost, thank you for your ${user_pay}! 😂")


if __name__ == "__main__":
    print("Welcome to the you ain't winning lottery!")
    print("If you win, which you never will, you will win a million dollars\n")

    lottery = Lottery()
    lottery.play()

