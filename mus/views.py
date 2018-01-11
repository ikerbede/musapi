from django.core import serializers
from django.http import JsonResponse

# Create your views here.

from mus import models

def users(request):
  if request.method == 'GET':
    data = models.User.objects.all()
    status = 200
  elif request.method == 'POST':
    data = {}
    status = 201
  elif request.method == 'PUT':
    data = {}
    status = 200
  elif request.method == 'DELETE':
    data = {}
    status = 204
  dataJson = serializers.serialize('json', data)
  return JsonResponse(status=status, data=dataJson, safe=False)

def messages(request):
  if request.method == 'GET':
    data = models.Message.objects.all()
    status = 200
  elif request.method == 'POST':
    data = {}
    status = 201
  dataJson = serializers.serialize('json', data)
  return JsonResponse(status=status, data=dataJson, safe=False)

def teams(request):
  if request.method == 'GET':
    data = models.Team.objects.all()
    status = 200
  elif request.method == 'POST':
    data = {}
    status = 201
  dataJson = serializers.serialize('json', data)
  return JsonResponse(status=status, data=dataJson, safe=False)

def rounds(request):
  if request.method == 'GET':
    data = models.Round.objects.all()
    status = 200
  elif request.method == 'POST':
    data = {}
    status = 201
  dataJson = serializers.serialize('json', data)
  return JsonResponse(status=status, data=dataJson, safe=False)

def scores(request):
  if request.method == 'GET':
    data = models.Score.objects.all()
    status = 200
  elif request.method == 'POST':
    data = {}
    status = 201
  dataJson = serializers.serialize('json', data)
  return JsonResponse(status=status, data=dataJson, safe=False)
