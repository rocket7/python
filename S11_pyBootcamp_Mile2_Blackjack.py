#!/usr/bin/python

# Python Bootcamp - Blackjack Game
# https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/08-Milestone%20Project%20-%202/01-Milestone%20Project%202%20-%20Assignment.ipynb

import random
import sys

"""
In this milestone project you will be creating a Complete BlackJack Card Game in Python.
Here are the requirements:
You need to create a simple text-based BlackJack game
The game needs to have one player versus an automated dealer.
The player can stand or hit.
The player must be able to pick their betting amount.
You need to keep track of the player's total money.
You need to alert the player of wins, losses, or busts, etc...
And most importantly:
You must use OOP and classes in some portion of your game. You can not just use functions in your game. Use classes to help you define the Deck and the Player's hand. There are many right ways to do this, so explore it well!
Feel free to expand this game. Try including multiple players. Try adding in Double-Down and card splits! Remember to you are free to use any resources you want and as always:
"""

## GLOBALS

total_hands = 0


class Player():

    def __init__(self, name):
        self.name = name
        self.cards = []
        self.wallet = None
        self.wins = 0
        self.hands = 0
        self.bet = 0


    def bet(self, bet_amount):
        self.wallet.withdrawl(bet_amount)


class Account():

    def __init__(self, amount):
        self.balance = amount



    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount


    def withdrawl(self, amount):
        if self.balance - amount < 0:
            print("Withdrawl will result in negative balance - please select smaller amount")
        else:
            self.balance -= amount






class Deck():

    def __init__(self, deck_count=1):
        self.deck_count = deck_count
        self.deck = []
        self.suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
        self.card_number = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
        self.card_value = [2,3,4,5,6,7,8,9,10,10,10,10,11]

    def shuffle_deck(self):
        pass

    def display_hand(self, player_name, card_hand):
        total = 0
        print(f"{player_name} has following hand:")
        for x in card_hand:
            print(f"\t {x[0]} of {x[1]}")
            total += x[2]
        print(f"For a total hand count of {total}")


    def create_deck(self):
        # Create Card Deck as List of Tuples
        for suit in self.suits:
            count = 0
            for card in self.card_number:
                self.deck.append((card, suit, self.card_value[count]))
                count += 1


    def print_hand(self, hand):
        print(hand)

    def count_hand(self, card_hand):
        hand_count = 0
        for x in card_hand:
            if x[0] == 'Ace':
                value = input("Please select value for Ace (1 or 11): ")
                if value == 1 or value == 11:
                    hand_count += int(value)
                else:
                    print("Error entering value for Ace")
            else:
                hand_count += x[2]
        return hand_count


    def deal_hand(self, cards):
        random.shuffle(self.deck)
        c = 0
        hand = []
        while c < cards:
            hand.append(self.deck.pop(c))
            print(f"hand: {hand}")
            c += 1
        return hand




# ACE CAN BE 1 or 11

class Blackjack(Deck):

    def __init__(self):
        Deck.__init__(self) #NO COLON AND NO INDENT FOR PASS  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        pass










if __name__ == '__main__':

    #Create Deck
    b = Blackjack()
    b.create_deck()

    while True:
        intro = input("Would you like to play a game of blackjack? [y|n]")
        if intro == 'y':
            break
        elif intro == 'n':
            sys.exit()
        else:
            print("Invalid selection...")


    # List of Player Objects
    players = []

    while True:
        player_count = input("How many players?")
        for x in range(0,int(player_count)):
            players.append(Player("Player" + str(x + 1),))
        break


    # Add 100 to each players account
    for x in players:
        x.wallet = Account(100)

    print(f"Players: {players[0].name}")


    while True:
        bet_amount = input("Please place your bets..")
        for x in range(0,int(player_count)):
            print("Player{} please place your bet: ".format(x + 1))
            players[x].wallet.withdrawl(int(bet_amount))
        break


    dealer_acct = Account(100)
    dealer = Player("Dealer")
    dealer.cards = b.deal_hand(2)

    while True:
        for x in range(0,int(player_count)):
            players[x].cards = b.deal_hand(2)
        break


    while True:
        for x in range(0,int(player_count)):
            print("Player{} card count is {}".format(x + 1, b.count_hand(players[x].cards)))
        break




    #print("P1")
    #print(p1.cards)
    #print(b.count_hand(p1.cards))
    #print(p1.wallet.balance)

    #print(b.count_hand(player1_hand))
    #b.display_hand("player1",player1_hand)
    #dealer_hand = b.deal_hand(2)
    #print(b.count_hand(dealer_hand))
    #print(len(b.deck))

