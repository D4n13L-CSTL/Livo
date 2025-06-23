# calendario/models.py
from django.db import models
from clubes.models import Club

class EventoCalendario(models.Model):
    TIPO_EVENTO = [
        ('ENTRENAMIENTO', 'Entrenamiento'),
        ('PARTIDO', 'Partido'),
        ('REUNION', 'Reunión'),
        ('EVENTO', 'Evento especial'),
    ]
    
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    inicio = models.DateTimeField()
    fin = models.DateTimeField()
    tipo_evento = models.CharField(max_length=20, choices=TIPO_EVENTO)
    
    def __str__(self):
        return f"{self.titulo} ({self.club})"