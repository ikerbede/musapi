from random import choice
from color import Color
from hand import Hand

class Deck:
  def __init__(self):
    self.cards = (Color().cards + Color().cards) + (Color().cards + Color().cards)

  def removeCard(self):
    card = choice(self.cards)
    self.cards.remove(card)
    return card

  def dealCards(self):
    hands = [Hand(), Hand(), Hand(), Hand()]
    for hand in hands:
      for i in range (1, 5):
        hand.addCard(self.removeCard())
      hands.append(hand)
    return hands

  def getCards(self, nb):
    cards = []
    if (nb > len(self.cards)):
      raise IndexError('You try to remove more cards than it remains in card deck!')
    for i in range(0, nb):
      cards.append(self.removeCard())
    return cards

