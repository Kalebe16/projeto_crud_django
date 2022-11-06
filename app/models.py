from django.db import models


# Create your models here.
class Carros(models.Model):
    modelo = models.CharField(max_length=60)
    marca = models.CharField(max_length=40)
    ano = models.IntegerField()
    
