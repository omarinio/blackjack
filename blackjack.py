import random
import copy

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4

def card_check(card):
	if card == 11:
		card = 'J'
	elif card == 12:
		card = 'Q'
	elif card == 13:
		card = 'K'
	elif card == 14:
		card = 'A'
	return card 
		

def hit(hand):
	card = deck.pop(0)
	hand.append(card_check(card))
	return hand
	
def total(hand):
	total = 0
	numerical_hand = copy.deepcopy(hand) 
	for index, card in enumerate(numerical_hand):
		if card == 'J' or card == 'Q' or card == 'K':
			numerical_hand[index] = 10
		elif card == 'A':
			numerical_hand[index] = 11
			
	for card in sorted(numerical_hand):
		if card == 11:
			if total >= 11:
				total+= 1
			else:
				total+= 11
		else:
			total += card
			
	return total
	
def print_scores(hand, dealer):
	print("The dealer has " + str(dealer) + "with a total score of " + str(total(dealer)))
	print("You have " + str(hand) + "with a total score of " + str(total(hand)))
	
def game_over_check(hand, dealer):
	is_game_over = 0
	
	if total(hand) == 21 and total(dealer) == 21:
		is_game_over = 1
	elif total(hand) == 21: 
		is_game_over = 1
	elif total(dealer) == 21: 
		is_game_over = 1
	elif total(hand) > 21:
		is_game_over = 1
	elif total(dealer) > 21:
		is_game_over = 1
	return is_game_over
	
def game_over(hand, dealer):
	if total(hand) == 21 and total(dealer) == 21:
		print("Both players got a blackjack! The round is a draw\n")
		print_scores(hand, dealer)
	elif total(hand) == 21: 
		print("You got a blackjack! You win!\n")
		print_scores(hand, dealer)
	elif total(dealer) == 21: 
		print("The dealer got a blackjack! You lose!\n")
		print_scores(hand, dealer)
	elif total(hand) > 21:
		print("You busted! You lose!\n")
		print_scores(hand, dealer)
	elif total(dealer) > 21:
		print("The dealer busted! You win!\n")
		print_scores(hand, dealer)
	elif total(hand) > total(dealer):
		print("Your hand is greater than the dealer's! You win!\n")
		print_scores(hand, dealer)
	elif total(dealer) > total(hand):
		print("The dealer's hand is greater than your's! You lose!\n")
		print_scores(hand, dealer)
	elif total(dealer) == total(hand):
		print("The dealer's hand is the same as your's! Its a draw!\n")
		print_scores(hand, dealer)
	
	exit()

def starting_hand(hand, dealer):
	card = deck.pop(0)
	hand.append(card_check(card))
	card = deck.pop(0)
	dealer.append(card_check(card))
	card = deck.pop(0)
	hand.append(card_check(card))
	card = deck.pop(0)
	dealer.append(card_check(card))


def game():
	hand = []
	dealer = []
	move = 0
	
	answer = input('Welcome to Blackjack, would you like to play? y/n \n').lower()
	if answer == 'y':
		random.shuffle(deck)
		
		starting_hand(hand, dealer)
		while move != 's':
			print("The dealers hand is " + str(dealer) + "for a total of " + str(total(dealer)) + "\n")
			print("Your hand is " + str(hand) + "for a total of " + str(total(hand)) + "\n")
			move = input('Would you like to [H]it or [S]tand ').lower()
			if move == 'h':
				hit(hand)
				if game_over_check(hand, dealer) == 1:
					game_over(hand, dealer)
			elif move == 's':
				while total(dealer) < 17:
					hit(dealer)
				game_over(hand, dealer)
		
game()
