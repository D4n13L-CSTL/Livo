# clubes/models.py
from django.db import models
from usuarios.models import Usuario
from deportes.models import Deporte

class Club(models.Model):
    nombre = models.CharField(max_length=200)
    direccion_club = models.TextField()
    logo = models.ImageField(upload_to='clubes/logos/', null=True, blank=True)
    deporte = models.ForeignKey(Deporte, on_delete=models.PROTECT)
    año_fundacion = models.PositiveIntegerField()
    ubicacion = models.CharField(max_length=255, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

    



class AdministradorClub(models.Model):
    email = models.EmailField(unique=True, null=True, blank=True)
    nombre_completo = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    usuario = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE, related_name='club')

    def __str__(self):
        return f"{self.nombre_completo} ({self.club.nombre})"