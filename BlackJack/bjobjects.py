import cards
class BJCard(cards.Card):
    """ a standard Blackjack Card """
    ACEVALUE = 1
    
    @property
    def value(self):
        if(self.faceUp):
            v = BJCard.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10
        else:
            v = None
        return v

class BJHand(cards.Hand):
    """ a standard Blackjack Player """

    def __init__(self, name):
        super(BJHand, self).__init__()
        self.name = name

    def __str__(self):
        rep = self.name + ":" + super(BJHand, self).__str__()
        if self.total:
            rep += "(" + str(self.total) + ")"
        return rep

    @property
    def total(self):
        
        for card in self.cards:
            if not card.value:
                return None

        t = 0
        for card in self.cards:
            t += card.value

        containsAce = False
        for card in self.cards:
            if card.value == BJCard.ACEVALUE:
                containsAce = True

        if containsAce and t <= 11:
            t += 10

        return t

class BJDeck(cards.Deck):
    """ a standard Deck in Blackjack """

    def populate(self):
        for suit in BJCard.SUITS:
            for rank in BJCard.RANKS:
                self.cards.append(BJCard(rank, suit))

class BJPlayer(BJHand):
    """ a Blackjack Player"""

    def isHitting(self):
        response = input("Would you like to hit? (Y/N)")
        return response == "y"

    def bust(self):
        print(self.name, "busts")

    def isBusted(self):
        print(self.total)
        return self.total > 21

    def lose(self):
        print(self.name, "loses")

    def win(self):
        print(self.name, "wins")

    def push(self):
        print(self.name, "pushes")



class BJDealer(BJHand):
    """ The dealer in Blackjack"""

    def isHitting(self):
        return self.total < 17

    def isBusted(self):
        print(self.total)
        return self.total > 21

    def bust(self):
        print(self.name, "busts")

    def flipFirstCard(self):
        firstCard = self.cards[0]
        firstCard.flip()

class BJGame(object):
    """ a game of blackjack """

    def __init__(self, names):
        self.players = []
        for name in names:
            player = BJPlayer(name)
            self.players.append(player)

        self.dealer = BJDealer("Dealer")

        self.deck = BJDeck()
        self.deck.populate()
        self.deck.shuffle()

    def stillPlaying(self):
        sp = []
        for player in self.players:
            if not player.isBusted():
                sp.append(player)
        return sp

    def __additional_cards(self, player):
        while not player.isBusted() and player.isHitting():
            self.deck.deal([player])
            print(player)
            if player.isBusted():
                player.bust()

    def play(self):
        
        self.deck.deal(self.players + [self.dealer], cardsPerHand = 2)
        self.dealer.flipFirstCard()
        for player in self.players:
            print(player)
        print(self.dealer)

        for player in self.players:
            self.__additional_cards(player)

        self.dealer.flipFirstCard()

        if not self.stillPlaying():
            print(self.dealer)
        else:
            print(self.dealer)
            self.__additional_cards(self.dealer)

            if self.dealer.isBusted():
                for player in self.stillPlaying():
                    player.win()
            else:
                for player in self.stillPlaying():
                    if player.total > self.dealer.total:
                        player.win()
                    elif player.total < self.dealer.total:
                        player.lose()
                    else:
                        player.push()
        for player in self.players:
            player.clear()
        self.dealer.clear()