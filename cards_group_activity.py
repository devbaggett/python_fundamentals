import random

class Deck(object):
	def __init__(self):
		self.allCard = []
		self.create()

	def create(self):
		suits = ["clubs", "diamonds", "hearts", "spades"]

		for i in range(1, 14):
			for j in range(0, 4):
				newCard = Card(suits[j], i)
				self.allCard.append(newCard)

	def shuffle(self):
		random.shuffle(myfirstdeck.allCard)
		print self.allCard


class Card(object):
	def __init__(self, suits, pips):
		self.suits = suits
		self.pips = pips

myfirstdeck = Deck()


myfirstdeck.shuffle()

print myfirstdeck.allCard[0].suits


print len(myfirstdeck.allCard)


