from kolore import Kolore

from random import choice

class Esku():
  def __init__(self):
    self.cards = []
  
  def addCard(self, card):
    if (card not in Kolore().cards):
      raise ValueError("Unexpected card!")
    elif (len(self.cards) == 4):
      raise IndexError("Eskua is full already!")
    else:
      self.cards.append(card)
      self.cards.sort()

  def getPairValuesAndPoints(self):
    vap = []
    value = 0
    points = 0
    for card in self.cards:
      if (card <> value):
        nbOccurences = self.cards.count(card)
        if (nbOccurences > 1):
          value = card
          if (nbOccurences == 2):
            points = 1
          elif (nbOccurences == 3):
            points = 2
          elif (nbOccurences == 4):
            points = 3
          else:
            raise ValueError("Unexpected number of occurences: " + nbOccurences)
          vap.append([value, points])
    
    return vap
  
  def getGameValueAndPoints(self):
    vap = []
    value = 0
    for card in self.cards:
      if (card in [11, 12]):
        value += 10
      else:
        value += card
    vap.append(value)

    if (value < 31):
      vap.append(1)
    elif (value > 31):
      vap.append(2)
    elif (value == 31):
      vap.append(3)
    
    return vap

  def removeCards(self, cards):
    for card in cards:
      self.cards.remove(card)
