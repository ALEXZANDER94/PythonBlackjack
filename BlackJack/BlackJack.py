import cards
import bjobjects
import os

bjDeck = cards.Deck()

bjDeck.populate()

bjDeck.shuffle()


#main
def main():
    print("Welcome to Blackjack")

    names = []
    number = int(input("How many players are playing? "))
    for i in range(number):
        name = input("Enter player name: ")
        names.append(name)

    print()

    game = bjobjects.BJGame(names)

    again = None
    while again != "n":
        os.system('cls')
        game.play()
        again = input("Would you like to play again? ")

main()

