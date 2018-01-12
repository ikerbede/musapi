from django.db import models

class Round(models.Model):

  class Meta:
    db_table = 'Round'
    managed = False

  id = models.AutoField(primary_key=True)
  team1Id = models.SmallIntegerField()
  team2Id = models.SmallIntegerField()
  date = models.DateField()
