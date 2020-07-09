import time
class Card(object):
    """ a regular card in a card game"""

    #Each card will have a Rank (A-K) and a Suit (diamond, club, spade, heart)
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["D", "H", "C", "S"]

    #the constructor takes a rank and a suit and creates a new card from it
    def __init__(self, rank, suit, faceUp = True):
        self.rank = rank
        self.suit = suit
        self.faceUp = faceUp

    #so if print(<object>) is called, the card will print the rank and suit
    def __str__(self):
        if self.faceUp:
            rep = self.rank + self.suit
        else:
            rep = "XX"
        return rep

    def flip(self):
        self.faceUp = not self.faceUp


class Hand(object):
    """ a standard hand in a card game"""

    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + " "
        else:
            rep = "<empty>"
        return rep

    def add(self, card):
        self.cards.append(card)

    def clear(self):
        self.cards = []

    def give(self, card, otherHand):
        self.cards.remove(card)
        otherHand.add(card)

class Deck(Hand):
    """ a deck of cards in a card game"""

    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.cards.append(Card(rank, suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, players, cardsPerHand = 1):
        for rounds in range(cardsPerHand):
            for player in players:
                if self.cards:
                    topCard = self.cards[0]
                    self.give(topCard, player)
                else:
                    print("Out of cards")
