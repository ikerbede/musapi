from django.core import serializers
from django.http import JsonResponse

# TODO
# GET /hands --> get 4 hands from the current card deck (includes pairs and game for each hand)
# POST /hands --> send mus resulted partial hands and get new full hands (same formar with pairs and game) 

def hands(request):
  if request.method == 'GET':
    deck = Deck()
    hands = deck.dealCards()
    data = []
    for hand in hands:
      data.append(hand.toJson())
    status = 200
  dataJson = serializers.serialize('json', data)
  return JsonResponse(status=status, data=dataJson, safe=False)
