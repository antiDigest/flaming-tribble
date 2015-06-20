from django.db import models

# Create your models here.
class Words(models.Model):
    word = models.CharField(max_length=200)
    genericity = models.BooleanField()
    frequency = models.IntegerField(default=0)
    trend = models.IntegerField(range(1,3), default=3)

class Searched(models.Model):
    word = models.CharField(max_length=200)
    genericity = models.BooleanField()
    frequency = models.IntegerField(default=0)
    trend = models.ForeignKey(Words)