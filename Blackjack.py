import Deck
import Player

print "Type your name."
yourName = raw_input()
yourMoney = 10000

newdeck = Deck.Deck()
newdeck.shuffle()
dealer = Player.Player("The Dealer", 10000)
player1 = Player.Player(yourName, yourMoney)

def round():
    over = False  # if any victory condition is reached, this becomes true
    newdeck.shuffle()  # do you shuffle the deck after every hand?
    dealer.deal(newdeck)
    player1.deal(newdeck)
    p1score = player1.score
    while over is False:
        if dealer.stay is True:
            if player1.score > dealer.score:
                print "You win!"
                over = True
                return 1
        if player1.stay is True:
            if player1.score < dealer.score:
                print "The Dealer wins!"
                over = True
                return 0
        if dealer.stay is False:
            dealer.autoTurn(newdeck, p1score)
            if dealer.score == 21:
                if player1.score == 21:
                    print "It's a perfect draw!"
                    over = True
                    return -1
                else:
                    print "The Dealer wins!"
                    over = True
                    return 0
            elif dealer.score > 21:
                print "The Dealer busts!"
                over = True
                return 1
        if player1.stay is False:
            if player1.score == 21:
                if dealer.score == 21:
                    print "It's a perfect draw!"
                    over = True
                    return -1
                else:
                    print "You win!"
                    over = True
                    return 1
            if player1.score > 21:
                print "You bust!"
                over = True
                return 0
            player1.turn(newdeck)
            p1score = player1.score
        if dealer.stay is True and player1.stay is True:
            if player1.score > dealer.score:
                print "You win!"
                over = True
                return 1
            if player1.score < dealer.score:
                print "The Dealer wins!"
                over = True
                return 0
            if player1.score == dealer.score:
                print "It's a draw!"
                over = True
                return -1

def game():
    while dealer.money > 0 and player1.money > 0:
        player1.bet = 0
        player1.stay = False
        dealer.stay = False
        print "You have " + str(player1.money) + " dollars, and the Dealer has " + str(dealer.money) + " dollars."
        print "How much would you like to bet?"
        while player1.bet == 0:
            try:
                bet = int(input())
                print bet
                player1.bet = bet
                break
            except:
                print "I need a number."
            '''if bet is int:
                if bet > 0:'''
            '''else:
                print "Please enter a positive number."
            else:
                print "Please enter a number."'''
        print "past the loop"
        victory = round()
        if victory == 1:
            print "You won your bet of " + str(player1.bet) + " dollars!"
            player1.money += player1.bet
            dealer.money -= player1.bet
        if victory == 0:
            print "You lost your bet of " + str(player1.bet) + " dollars!"
            player1.money -= player1.bet
            dealer.money += player1.bet
        if victory == -1:
            print "You tied, no money."
    if dealer.money <= 0:
        print "You win all the money!"
    if player1.money <= 0:
        print "You're out of money"

game()
k = input("Press exit to close.")