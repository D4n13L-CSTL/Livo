# clubes/models.py
from django.db import models
from usuarios.models import Usuario
from deportes.models import Deporte
from atletas.models import Atleta
import uuid

class Club(models.Model):
    nombre = models.CharField(max_length=200)
    serial_club = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
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
    


class ClubAtleta(models.Model):
    atleta = models.ForeignKey(Atleta,on_delete=models.CASCADE,related_name='inscripciones_atletas')
    club = models.ForeignKey(Club,on_delete=models.CASCADE, related_name='clubes_disponibles')
    fecha_registro = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    fecha_baja = models.DateTimeField(null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['atleta'],
                condition=models.Q(activo=True),
                name='unique_atleta_activo'
            )
        ]

    def save(self, *args, **kwargs):
        if self.activo:
            # Desactivar cualquier otra membresía activa
            ClubAtleta.objects.filter(atleta=self.atleta, activo=True).update(activo=False)
        super().save(*args, **kwargs)