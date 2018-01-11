from kolore import Kolore
from joku import Joku
from esku import Esku

def main():
  jokua = Joku()
  print jokua.cards
  eskuak = jokua.dealCards()
  print jokua.cards
  for esku in eskuak:
    print esku.cards
    print esku.getPairValuesAndPoints()
    print esku.getGameValueAndPoints()

main()