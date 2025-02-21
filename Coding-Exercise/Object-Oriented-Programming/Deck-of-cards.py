# There are many card games that you could implement in Python: poker, war, blackjack...
# Naturally, implementing an entire card game is a long and complicated process.
# In this exercise, we're only going to focus on a tiny part that could be used in many card games:
# implementing a deck of cards using OOP with some basic, ready-to-use operations.

# Your task is to implement two classes: Card and Deck. The Deck should be a standard 52-card deck 
# as described here: wiki page.

# The Card should be a very simple class with just two attributes: suit and value.
# It should also have a method named present() that returns a string showing {value} of {suit}.
# For instance, for a card created in the following way Card('hearts', '10') the method should return  10 of hearts.

# The Deck should have one attribute: cards. It should be a list of Card objects representing a full card deck
# with all combinations of suits and values. For your convenience, here are the exact values that should be used:

# suits = ['hearts', 'diamonds', 'clubs', 'spades']
# values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
# In other words, the Deck should internally have a cards list with card objects such as Card('hearts', 'Ace') 
# or Card('spades', '5'). When created, each object of the Deck class should have exactly 52 cards, 
# one of each value and suit.

# The Deck class should also make available the following methods:

# 1. shuffle(): this method should randomly change the order of cards in the deck*

# 2.  deal(): this method should return one card object from the Deck (the currently last card in the cards list)
# and then also remove that object from the Deck. If there are no cards left, return None.

# 3. count_remaining(): this method should return the number of cards (an integer) in the deck

# 4. get_remaining(): this method should return a list of strings, each string describing a single remaining card,
# using the present() method for the Card class described above. 
# For instance, if there are two cards remaining in the deck, the returned list could look as follows (the remaining cards shown below are picked at random):

# ['3 of hearts', 'Jack of spades']
# * You can use the shuffle method from the random module like this: random.shuffle(list_name)


import random 
from itertools import product  # Importing itertools.product to generate card combinations

# Card class represents an individual playing card
class Card:
    def __init__(self, suit, value):
        """
        Initializes a Card object. Example: Card("hearts", "10")
        """
        self.suit = suit  # Suit of the card (hearts, diamonds, clubs, spades)
        self.value = value  # Value of the card (Ace, 2, 3, ..., King)

    def present(self):
        return f"{self.value} of {self.suit}"

# Deck class represents a full deck of 52 playing cards
class Deck:
    def __init__(self):
        """
        Initializes a Deck object with a full set of 52 unique cards.
        """
        suits = ['hearts', 'diamonds', 'clubs', 'spades']
        values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

        # Creating all 52 Card objects and storing them in the cards list
        self.cards = [Card(suit, value) for suit, value in product(suits, values)]

    def shuffle(self):
        random.shuffle(self.cards)  # Shuffles the deck of cards randomly.

    def deal(self):
        return self.cards.pop() if self.cards else None  # Removes and returns last card or None if empty

    def count_remaining(self):
        return len(self.cards) # Returns the number of cards left in the deck.

    def get_remaining(self):
        return [card.present() for card in self.cards]  # Converts each Card object into a string


deck = Deck()  
deck.shuffle()  

card1 = deck.deal()  
print(card1.present() if card1 else "No more cards")  

print(f"Cards left: {deck.count_remaining()}")  

print(deck.get_remaining())  

