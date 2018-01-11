from django.db import models

# Create your models here.

class User(models.Model):

  class Meta:
    db_table = 'User'
    managed = False

  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=100)
  password = models.CharField(max_length=30)
  avatar = models.CharField(max_length=100, blank=True)

class Message(models.Model):

  class Meta:
    db_table = 'Message'
    managed = False

  id = models.AutoField(primary_key=True)
  userId = models.SmallIntegerField()
  date = models.DateTimeField()
  text = models.TextField()

class Team(models.Model):

  class Meta:
    db_table = 'Team'
    managed = False

  id = models.AutoField(primary_key=True)
  user1Id = models.SmallIntegerField()
  user2Id = models.SmallIntegerField()

class Round(models.Model):

  class Meta:
    db_table = 'Round'
    managed = False

  id = models.AutoField(primary_key=True)
  team1Id = models.SmallIntegerField()
  team2Id = models.SmallIntegerField()
  date = models.DateField()

class Score(models.Model):

  class Meta:
    db_table = 'Score'
    managed = False

  id = models.AutoField(primary_key=True)
  teamId = models.SmallIntegerField()
  roundId = models.IntegerField()
  value = models.SmallIntegerField()
