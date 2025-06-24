# usuarios/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    TIPO_USUARIO = [
        ('ADMIN', 'Administrador'),
        ('CLUB', 'Administrador de Club'),
        ('ATLETA', 'Atleta'),
    ]
    
    tipo_usuario = models.CharField(max_length=10, choices=TIPO_USUARIO)
    telefono = models.CharField(max_length=20, blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']