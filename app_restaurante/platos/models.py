from django.db import models

# Create your models here.

class Platos(models.Model):
    nombre = models.CharField(max_length=35)
    precio = models.IntegerField()

