from random import choice
from kolore import Kolore
from esku import Esku

class Joku:
  def __init__(self):
    self.cards = (Kolore().cards + Kolore().cards) + (Kolore().cards + Kolore().cards)

  def removeCard(self):
    card = choice(self.cards)
    self.cards.remove(card)
    return card

  def dealCards(self):
    eskuak = [Esku(), Esku(), Esku(), Esku()]
    for esku in eskuak:
      for i in range (1, 5):
        esku.addCard(self.removeCard())
      eskuak.append(esku)
    return eskuak

  def getCards(self, nb):
    cards = []
    for i in range(0, nb):
      cards.append(self.removeCard())
    return cards

