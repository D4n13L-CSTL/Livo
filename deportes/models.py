# deportes/models.py
from django.db import models

class Deporte(models.Model):
    nombre = models.CharField(max_length=100)
    #descripcion = models.TextField(blank=True)
    #imagen = models.ImageField(upload_to='deportes/', null=True, blank=True)
    
    def __str__(self):
        return self.nombre