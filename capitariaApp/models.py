from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=80)
    promedio = models.IntegerField()

