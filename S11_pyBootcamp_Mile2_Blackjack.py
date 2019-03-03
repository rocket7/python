#!/usr/bin/python

# Python Bootcamp - Blackjack Game
# https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/08-Milestone%20Project%20-%202/01-Milestone%20Project%202%20-%20Assignment.ipynb

import random
import sys
#import pyforms
#import tkinter

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
        self.hand = [0][0]
        self.wallet = None
        self.wins = 0
        self.losses = 0
        self.push = 0
        self.total = 0
        self.bet_amount = 0
        self.hand_count = 0


    def bet(self, bet_amount):
        self.wallet.withdrawl(bet_amount)

    def win(self, bet_amount):
        self.wallet.deposit(bet_amount)


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
        self.card_number = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
        self.suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
        self.card_value = [2,3,4,5,6,7,8,9,10,10,10,10,11]

    def shuffle_deck(self):
        random.shuffle(self.deck)


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

    def count_hand(self, player_obj):
        player_obj.hand_count = 0
        for x in player_obj.cards:
            if x[0] == 'Ace':
                value = input("Please select value for Ace (1 or 11): ")
                if value == '11' and x[3] == 11:
                    player_obj.hand_count += int(value)
                    break
                elif value == '1' and x[3] == 11:
                    new_card = (x[0],x[1],1)
                    player_obj.cards.pop(x)
                    player_obj.cards.append(new_card)
                    #player_obj.cards[x][2] = int(value)
                    #x[2] = int(value) # CANNOT UPDATE VALUE OF TUPLE
                    player_obj.hand_count += int(value)
                else:
                    print("Error entering value for Ace")
            else:
                #print(f"Player {player_obj.name} has count of {player_obj.hand_count}")
                player_obj.hand_count += x[2]
        return player_obj.hand_count


    def deal_hand(self, cards):
        random.shuffle(self.deck)
        c = 0
        hand = []
        while c < cards:
            hand.append(self.deck.pop(c))
            #print(f"deal_hand: {hand}")
            c += 1
        return hand




# ACE CAN BE 1 or 11

class Blackjack(Deck):

    def __init__(self):
        Deck.__init__(self) #NO COLON AND NO INDENT FOR PASS  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


    def shuffle_deck(self):
        b.create_deck()


    def place_bet(self, player_obj):
        player_obj.bet_amount = input("Place Bet - Please place your bets..")
        print("{} has bet: ${}".format(player_obj.name, player_obj.bet_amount))
        player_obj.wallet.withdrawl(int(player_obj.bet_amount))
        #dealer_acct = Account(0)


    def winning_bet(self, player_obj):
        print("{} has won ${}".format(player_obj.name, player_obj.bet_amount * 2))
        player_obj.wallet.deposit(int(player_obj.bet_amount * 2))
        #dealer_acct = Account(0)


    # Move to Blackjack Class
    # Deal hand
    def deal_blackjack_hand(self, player_obj):
        #Deal Player Cards
        if player_obj.name == "Dealer":
            dealer.cards = b.deal_hand(2)
        else:
            player_obj.cards = b.deal_hand(2)


    # Evaluate hand
    def player_hand_count(self, player_obj):
        print("Dealer card displayed is {}".format(dealer.cards[0]))
        print("Player{} -----------------".format(player_obj.name))
        print("\tCards: {}".format(player_obj.cards))
        print("\tCards Total: {}".format(b.count_hand(player_obj)))
        while True:
            hit = input("Would you like hit? [y|n]")
            if hit == 'y':
                player_obj.cards.append(b.deck.pop())
                print("Player{} -----------------".format(player_obj.name))
                print("\tHit Player{} with Card {}".format(player_obj.name, player_obj.cards[-1]))
                print("Player{} card count is {}".format(player_obj.name, b.count_hand(player_obj)))
                #player_obj.hand_count = b.count_hand(player_obj)
            else:
                player_obj.hand_count = b.count_hand(player_obj)
                break


    def dealer_hand_count(self, dealer_obj):
        print("Dealer -----------------")
        print("\tThe dealer card count is {}".format(b.count_hand(dealer_obj)))
        while True:
            if int(b.count_hand(dealer_obj)) < 17:
                dealer.cards.append(b.deck.pop())
                print("Dealer -----------------")
                print("\tCards: {}".format(dealer_obj.cards))
                print("\tDealer card count is {}".format(b.count_hand(dealer_obj)))
                dealer_obj.hand_count = b.count_hand(dealer_obj)
            else:
                break


    def winning_hand(self, players, dealer_obj):
        print("++++++++++++++++++++++++++++++++++++++")
        print(f"Dealer has following hand:\n {dealer_obj.cards} Dealer has a total card count of: {dealer_obj.hand_count}")
        for x in range(0,int(player_count)):
            if players[x].hand_count == 21 and dealer_obj.hand_count == 21:
                print("{} -------------------------".format(players[x].name + 1))
                print("Push - Both Dealer and {} have Blackjack!!".format(players[x].name))
                players[x].total += 1
                players[x].push += 1
            elif players[x].hand_count == 21 and dealer_obj.hand_count < 21:
                print("{} -------------------------".format(players[x].name + 1))
                print("{} has Blackjack and is Winner!!".format(players[x].name))
                players[x].total += 1
                players[x].wins += 1
                b.winning_bet(players[x])
                break
            elif dealer_obj.hand_count == 21 and players[x].hand_count < 21:
                print("{} -------------------------".format(players[x].name + 1))
                print("{} has Blackjack and is Winner!!".format(dealer_obj.name))
                players[x].total += 1
                players[x].losses += 1
                break
            elif players[x].hand_count > dealer_obj.hand_count and players[x].hand_count < 21:
                print("{} -------------------------".format(players[x].name ))
                print("{} has better hand and is Winner!!".format(players[x].name))
                players[x].wins += 1
                players[x].total += 1
                b.winning_bet(players[x])
                break
            elif dealer_obj.hand_count > players[x].hand_count and dealer_obj.hand_count < 21:
                print("{} -------------------------".format(players[x].name ))
                print("{} has better hand and is Winner!!".format(dealer_obj.name))
                players[x].losses += 1
                players[x].total += 1
                break
            else:
                print("{} -------------------------".format(players[x].name))
                print("Push - Both Dealer and {} have same hand!!".format(players[x].name))
                players[x].total += 1
                break



if __name__ == '__main__':

    # List of Player Objects
    players = []
    dealer = Player("Dealer")

    #Create Deck
    b = Blackjack()

    while True:
        intro = input("Would you like to play a game of blackjack? [y|n]")
        if intro == 'y':
            while True:
                player_count = input("How many players?")
                for x in range(0,int(player_count)):
                    players.append(Player("Player" + str(x + 1)))
                    players[x].wallet = Account(100)

                break
            b.shuffle_deck()
            # Place Bets
            for x in range(0,int(player_count)):
                b.place_bet(players[x]) ##PASS PLAYERS OBJECT
            # Deal Player Cards
            for x in range(0,int(player_count)):
                b.deal_blackjack_hand(players[x])
            # Deal Dealer Cards
            b.deal_blackjack_hand(dealer)
            for x in range(0,int(player_count)):
                b.player_hand_count(players[x])
            b.dealer_hand_count(dealer)
            #for x in range(0,int(player_count)):
            b.winning_hand(players, dealer)
        elif intro == 'n':
            sys.exit()
        else:
            print("Invalid selection...")
            break


    print(f"Player Name: {players[0].name}")
    print(f"Player Balance: {players[0].wallet.balance}")


