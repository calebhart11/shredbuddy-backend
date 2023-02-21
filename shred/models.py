from django.db import models

# Create your models here.
class Session(models.Model):
    date = models.CharField(max_length=100)
    mountain = models.CharField(max_length=100)
    goals = models.CharField(max_length=400)