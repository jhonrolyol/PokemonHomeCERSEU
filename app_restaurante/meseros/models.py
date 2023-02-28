from django.db import models

# Create your models here.

class Meseros(models.Model):
    pais = models.CharField(max_length=50, default='')
    edad = models.IntegerField()
