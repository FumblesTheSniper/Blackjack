class Player(object):
    name = ""
    hand = []
    money = 0
    bet = 0
    score = 0
    stay = False

    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.hand = []
        self.score = 0
        self.stay = False

    def deal(self, deck):
        self.hand = []
        self.hand.append(deck.draw())
        self.hand.append(deck.draw())
        self.score = 0
        print self.name + "'s hand contains:"
        for card in self.hand:
            print card.nominal + " of " + card.suit
            self.score += card.val
        self.aceCheck()
        print "Total value: " + str(self.score)
        return self.score

    def hit(self, deck):
        print self.name + " is dealt another card."
        self.hand.append(deck.draw())
        self.score = 0
        print self.name + "'s hand now contains:"
        for card in self.hand:
            print card.nominal + " of " + card.suit
            self.score += card.val
        self.aceCheck()
        print "Total value: " + str(self.score)
        return self.score

    def aceCheck(self):  #Aces are either 1 or 11
        for card in self.hand:
            if self.score > 21:  # check score for each card so you only flip as many aces as you need to.
                if card.val == 11:
                    card.val = 1
                    self.score -= 10

    def autoTurn(self, deck, p1score):
        if self.score < 17 or self.score < p1score:  # dealer stays at 17, pretty standard
            self.hit(deck)
        else:
            print "The Dealer stays."
            self.stay = True
        return self.score

    def turn(self, deck):
        turn = False
        while turn is False:
            print "Would you like to hit or stay?"
            answer = raw_input()
            if answer in ["hit", "hit me", "Hit", "Hit me"]:
                self.hit(deck)
                turn = True
                break
            elif answer in ["stay", "stand", "Stay", "Stand"]:
                print self.name + " stays."
                self.stay = True
                turn = True
                break
            else:
                print "Type 'hit' or 'stay' please."
        return self.score


