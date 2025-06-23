# notificaciones/models.py
from django.db import models
from clubes.models import Club
from atletas.models import Atleta

class Notificacion(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE, null=True, blank=True)
    atleta = models.ForeignKey(Atleta, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=200)
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)
    
    def __str__(self):
        return self.titulo