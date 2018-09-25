import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':11}

playing = True
#Youssef

class Card():
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return "{} of {}".format(self.rank,self.suit)

class Deck():
    def __init__(self):
        self.deck = []  
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    
    def __str__(self):
    	self.deckdisplay = ""
    	for card in self.deck:
        	self.deckdisplay +="{} of {}\n".format(card.rank,card.suit)
    	return self.deckdisplay

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        dealed_card = self.deck.pop()
        return dealed_card

class Hand():
    def __init__(self):
        self.cards = []  
        self.value = 0   
        self.aces = 0    
    
    def add_card(self,deck):
    	self.added_card = deck.deal()
    	self.cards.append(self.added_card)
    	self.value += values[self.added_card.rank]
    
    def adjust_for_ace(self):
        if self.added_card.rank == "Ace" and self.value > 21:
        	self.value -= -10

class Chips():
    def __init__(self):
        self.total = 100  
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):
	while True:
		try:
			taken_bet = int(input("Please enter the amount you want to bet:"))
		except:
			print("Please enter an integer only")
			continue
		else:
			if taken_bet > player_chips.total:
				print("You cannot exceed your total number of chips")
				continue
            elif taken_bet == 0:
                print("You cannot bet 0") 
                continue
			chips.bet = taken_bet
			break

def hit(deck,hand):
	hand.add_card(game_deck)
	hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing  
    
    while playing:
	    option = str(input("Do you want to hit(h) or stand(s)?"))
	    if option.lower() == "h":
	    	hit(deck,hand)
	    	print("You recived {} of {}".format(hand.added_card.rank,hand.added_card.suit))
	    	print("Your hand value is {}".format(hand.value))
	    	continue
	    elif option.lower() == "s":
	    	playing = False
	    else:
	    	print("Please enter h or s")
	    	continue

def show_some(player,dealer):

	print("The dealer's card is:")
	print("{} of {}".format(dealer.cards[0].rank,dealer.cards[0].suit))
    
	print("The player's cards are:")
	for card in player.cards:
		print("{} of {}".format(card.rank,card.suit))
	print("The player's hand value is {}".format(player.value))
    
def show_all(player,dealer):

	print("The dealer's card are:")
	for card in dealer.cards:
		print("{} of {}".format(card.rank,card.suit))
	
    
	print("The player's cards are:")
	for card in player.cards:
		print("{} of {}".format(card.rank,card.suit))

def player_busts(player):
    if player.value > 21:
    	return True
    else:
    	return False

def player_wins(player,dealer):
    if player_busts(player) == False and (player.value > dealer.value or dealer_busts(dealer) == True):
    	return True
    else:
    	return False

def dealer_busts(dealer):
    if dealer.value > 21:
    	return True
    else:
    	return False

def dealer_wins(player,dealer):
    if dealer_busts(dealer) == False and (dealer.value > player.value or player_busts(player) == True):
    	return True
    else:
    	return False
    
def push(player,dealer,chips):
    if player_wins(player,dealer) == True or dealer_busts(dealer) == True:
    	print("The player has won!")
    	chips.win_bet()
    else:
    	print("The dealer has won!")
    	chips.lose_bet()


print("Welcome to Tareq's Black Jack Game!")

        
player_chips = Chips()
    
while True:  
    game_deck = Deck()
    game_deck.shuffle()

    player_hand = Hand()
    dealer_hand = Hand()

    player_hand.add_card(game_deck)
    player_hand.adjust_for_ace()
    player_hand.add_card(game_deck)
    player_hand.adjust_for_ace()

    dealer_hand.add_card(game_deck)
    dealer_hand.adjust_for_ace()
    dealer_hand.add_card(game_deck)
    dealer_hand.adjust_for_ace()
        
    # Set up the Player's chips

    take_bet(player_chips)
    show_some(player_hand,dealer_hand)  
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(game_deck,player_hand)
        
        
        # Show cards (but keep one dealer card hidden)
        #show_some(player_hand,dealer_hand)
 
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_busts(player_hand) == True:
        	print("The player has busted!")
        	break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        while dealer_hand.value < 17:
	        dealer_hand.add_card(game_deck)
	        dealer_hand.adjust_for_ace()

        show_all(player_hand,dealer_hand)
        print("The dealer's hand value is "+str(dealer_hand.value))
        print("The player's hand value is "+str(player_hand.value))

        if dealer_busts(dealer_hand) == True:
        	print("The dealer has busted!")
        	break
    
        # Show all cards
    
        # Run different winning scenarios
        player_wins(player_hand,dealer_hand)
        dealer_wins(player_hand,dealer_hand)
    
    push(player_hand,dealer_hand,player_chips)    
    # Inform Player of their chips total 
    print("The player's chips total is "+str(player_chips.total))

    
    # Ask to play again
    while True:
        again = str(input("Do you want to play again (y/n):"))
        
        if again.lower() == "y":
        	playing = True
        	break
        elif again.lower() == "n":
        	playing = False
        	exit()
        else:
        	print("Please enter y or n")
        	continue
