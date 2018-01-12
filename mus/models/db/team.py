from django.db import models

class Team(models.Model):

  class Meta:
    db_table = 'Team'
    managed = False

  id = models.AutoField(primary_key=True)
  user1Id = models.SmallIntegerField()
  user2Id = models.SmallIntegerField()
