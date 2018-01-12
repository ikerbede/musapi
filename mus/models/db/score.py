from django.db import models

class Score(models.Model):

  class Meta:
    db_table = 'Score'
    managed = False

  id = models.AutoField(primary_key=True)
  teamId = models.SmallIntegerField()
  roundId = models.IntegerField()
  value = models.SmallIntegerField()
