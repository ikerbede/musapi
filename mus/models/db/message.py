from django.db import models

class Message(models.Model):

  class Meta:
    db_table = 'Message'
    managed = False

  id = models.AutoField(primary_key=True)
  userId = models.SmallIntegerField()
  date = models.DateTimeField()
  text = models.TextField()
