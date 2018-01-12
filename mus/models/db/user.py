from django.db import models

class User(models.Model):

  class Meta:
    db_table = 'User'
    managed = False

  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=100)
  password = models.CharField(max_length=30)
  avatar = models.CharField(max_length=100, blank=True)
