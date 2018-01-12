from django.core import serializers
from django.http import JsonResponse

# TODO
# /teams --> all teams
# /teams/:teamId --> one team (users)
# /teams/:teamId/rounds --> all rounds of one team (includes scores)
# /teams/:teamId/rounds/:roundId --> one round of one team (includes score)

def teams(request):
  if request.method == 'GET':
    data = models.db.Team.objects.all()
    status = 200
  elif request.method == 'POST':
    data = {}
    status = 201
  dataJson = serializers.serialize('json', data)
  return JsonResponse(status=status, data=dataJson, safe=False)
