# atletas/models.py
from django.db import models
from deportes.models import Deporte

class Atleta(models.Model):
    usuario = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE, related_name='atleta')
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', null=True, blank=True)
    #password = models.CharField(max_length=128)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=20)
    descripcion = models.TextField(null=True, blank=True)
    

    def __str__(self):
        return f"{self.nombre}"




class AtletaDeporte(models.Model):
    NIVELES = [
        ('PRINCIPIANTE', 'Principiante'),
        ('INTERMEDIO', 'Intermedio'),
        ('AVANZADO', 'Avanzado'),
        ('PROFESIONAL', 'Profesional'),
    ]
    
    atleta = models.ForeignKey(Atleta, on_delete=models.CASCADE)
    deporte = models.ForeignKey(Deporte, on_delete=models.CASCADE)
    nivel_habilidad = models.CharField(max_length=20, choices=NIVELES, null=True, blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
  
