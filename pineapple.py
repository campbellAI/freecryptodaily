import sys
import numpy as np 

from card import Card
from deck import Deck
from evaluator import Evaluator


PAYOUT_MULTIPLIER = {
	"Royal Flush": 100,
	"Straight Flush": 40,
	"Four of a Kind": 7,
	"Full House": 5,
	"Flush": 4,
	"Straight": 3,
	"Three of a Kind": 2,
	"Two Pair": 1,
	"Pair": 0, #experiment w/ jacks/queens or better
	"High Card": 0
}

CARD_IMAGE_MAP = {
	"Ac": "static/icons/cards/clubs/ace.png",
	"2c": "static/icons/cards/clubs/two.png",
	"3c": "static/icons/cards/clubs/three.png",
	"4c": "static/icons/cards/clubs/four.png",
	"5c": "static/icons/cards/clubs/five.png",
	"6c": "static/icons/cards/clubs/six.png",
	"7c": "static/icons/cards/clubs/seven.png",
	"8c": "static/icons/cards/clubs/eight.png",
	"9c": "static/icons/cards/clubs/nine.png",
	"Tc": "static/icons/cards/clubs/ten.png",
	"Jc": "static/icons/cards/clubs/jack.png",
	"Qc": "static/icons/cards/clubs/queen.png",
	"Kc": "static/icons/cards/clubs/king.png",

	"Ad": "static/icons/cards/diamonds/ace.png",
	"2d": "static/icons/cards/diamonds/two.png",
	"3d": "static/icons/cards/diamonds/three.png",
	"4d": "static/icons/cards/diamonds/four.png",
	"5d": "static/icons/cards/diamonds/five.png",
	"6d": "static/icons/cards/diamonds/six.png",
	"7d": "static/icons/cards/diamonds/seven.png",
	"8d": "static/icons/cards/diamonds/eight.png",
	"9d": "static/icons/cards/diamonds/nine.png",
	"Td": "static/icons/cards/diamonds/ten.png",
	"Jd": "static/icons/cards/diamonds/jack.png",
	"Qd": "static/icons/cards/diamonds/queen.png",
	"Kd": "static/icons/cards/diamonds/king.png",

	"Ah": "static/icons/cards/hearts/ace.png",
	"2h": "static/icons/cards/hearts/two.png",
	"3h": "static/icons/cards/hearts/three.png",
	"4h": "static/icons/cards/hearts/four.png",
	"5h": "static/icons/cards/hearts/five.png",
	"6h": "static/icons/cards/hearts/six.png",
	"7h": "static/icons/cards/hearts/seven.png",
	"8h": "static/icons/cards/hearts/eight.png",
	"9h": "static/icons/cards/hearts/nine.png",
	"Th": "static/icons/cards/hearts/ten.png",
	"Jh": "static/icons/cards/hearts/jack.png",
	"Qh": "static/icons/cards/hearts/queen.png",
	"Kh": "static/icons/cards/hearts/king.png",

	"As": "static/icons/cards/spades/ace.png",
	"2s": "static/icons/cards/spades/two.png",
	"3s": "static/icons/cards/spades/three.png",
	"4s": "static/icons/cards/spades/four.png",
	"5s": "static/icons/cards/spades/five.png",
	"6s": "static/icons/cards/spades/six.png",
	"7s": "static/icons/cards/spades/seven.png",
	"8s": "static/icons/cards/spades/eight.png",
	"9s": "static/icons/cards/spades/nine.png",
	"Ts": "static/icons/cards/spades/ten.png",
	"Js": "static/icons/cards/spades/jack.png",
	"Qs": "static/icons/cards/spades/queen.png",
	"Ks": "static/icons/cards/spades/king.png"
}

def deal_starting_hand():
	deck = Deck()
	player_hand = deck.draw(3)
	return Card.print_pretty_cards(player_hand), deck


def play(wager, bankroll):
	#Starting Hand
	bankroll -= wager
	deck = Deck()
	player_hand = deck.draw(3)
	print("\nYour Starting Hand is:")
	print(Card.print_pretty_cards(player_hand))
	print("\nChoose 1 card to discard:")
	mapping = ""
	for i in range(3):
		mapping += f"{i + 1} - {Card.print_pretty_card(player_hand[i])}\n"
	print(mapping)
	discard = input("Discard: ")
	discard = int(discard)
	assert(discard in [1, 2, 3])
	player_hand = [c for i, c in enumerate(player_hand) if i != discard - 1]
	print(f"\nHole Cards: {Card.print_pretty_cards(player_hand)}\n")

	#Flop
	flop = deck.draw(3)
	print(f"Flop: {Card.print_pretty_cards(flop)}\n")
	if bankroll >= wager:
		double_down = input("Double Down? (y or n): ")
		assert(double_down in ["y", "n"])
		if double_down == "y":
			bankroll -= wager
			wager *= 2

	#Turn
	turn = deck.draw(1)
	print(f"\nTurn: {Card.print_pretty_card(turn)}\n")

	#River 
	river = deck.draw(1)
	print(f"River: {Card.print_pretty_card(river)}\n")

	#Evaluate hand strength
	board = flop + [turn] + [river]
	evaluator = Evaluator()
	score = evaluator.evaluate(board, player_hand)
	class_score = evaluator.get_rank_class(score)
	hand_rank = evaluator.class_to_string(class_score)
	if class_score == 1:
		hand_rank = "Royal Flush"
	print(f"Hand Rank: {hand_rank}\n")
	payout = int(wager*PAYOUT_MULTIPLIER[hand_rank])
	bankroll += payout

	return payout, bankroll


def main():
	bankroll = 100
	keep_playing = True
	while keep_playing:
		print(f"\nBankroll: {bankroll}\n")

		#wager = input(f"Place your wager (1-{bankroll}): ")
		wager = 10
		print(f"Wager: {wager}\n")
		assert(wager <= bankroll)
		assert(wager >= 1)
		payout, bankroll = play(wager, bankroll)
		print(f"\nPayout: {payout}\n")
		print(f"\nBankroll: {bankroll}\n")
		if bankroll < 1:
			print("You are out of money, thanks for playing!")
			sys.exit(0)
		else:
			kp = input("Keep playing? (enter y or n): ")
			assert(kp in ["y", "n"])
			keep_playing = True if kp == "y" else False

	print("\nThanks for playing!\n")


if __name__ == "__main__":
	main()














