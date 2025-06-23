# clubes/models.py
from django.db import models
from usuarios.models import Usuario
from deportes.models import Deporte

class Club(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    direccion_club = models.TextField()
    logo = models.ImageField(upload_to='clubes/logos/', null=True, blank=True)
    deporte = models.ForeignKey(Deporte, on_delete=models.PROTECT)
    año_fundacion = models.PositiveIntegerField()


    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre

    



class AdministradorClub(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    nombre_completo = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.nombre_completo} ({self.club.nombre})"