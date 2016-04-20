import random

suits = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

class Card(object):
    val = ""
    suit = ""
    nominal = ""

    def __init__(self, val, suit):
        self.val = val
        self.suit = suit
        if val < 11:
            self.nominal = str(val)
        elif val == 11:
            self.nominal = "Jack"
        elif val == 12:
            self.nominal = "Queen"
        elif val == 13:
            self.nominal = "King"
        elif val == 14:
            self.nominal = "Ace"
        if 10 < val < 14:  # need to set to proper values
            self.val = 10
        if val == 14:
            self.val = 11



class Deck(object):
    stack = []  # these cards are in the deck
    play = []   # these cards are in someone's hand
    discard = []

    def __init__(self):
        for s in suits:   # make the deck, standard 52 cards
            for v in values:
                newcard = Card(v, s)
                self.stack.append(newcard)

    def look(self):
        print "Cards in deck:"
        for card in self.stack:
            print str(card.nominal) + " of " + card.suit
        print "Cards in play:"
        for card in self.play:
            print str(card.nominal) + " of " + card.suit

    def shuffle(self):
        for i in self.play:
            self.stack.append(i)
            self.play.remove(i)
        for i in self.discard:
            self.stack.append(i)
            self.discard.remove(i)
        random.shuffle(self.stack)

    def draw(self):
        card = self.stack[0]  # draws the first card in the deck, puts it in play and removes from deck
        self.play.append(card)
        self.stack.remove(card)
        return card

