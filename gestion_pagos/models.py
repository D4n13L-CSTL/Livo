from django.db import models
from clubes.models import ClubAtleta
# Create your models here.

class Pago_Mensualida(models.Model):
    fecha_de_pago = models.DateField(auto_now_add=True)
    atleta_club = models.ForeignKey(ClubAtleta, on_delete=models.CASCADE)
    monto = models.FloatField()
    mes_correspondiente = models.DateField()
    foto_comprobante = models.ImageField(upload_to='comprobantes/', null=True, blank=True)
    confirmacion = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'Pago_Mensualidades'

class PagoInscripciones(models.Model):
    fecha_de_pago = models.DateField(auto_now_add=True)
    atleta_club = models.ForeignKey(ClubAtleta, on_delete=models.CASCADE)
    monto = models.FloatField()
    foto_comprobante = models.ImageField(upload_to='comprobantes/', null=True, blank=True)
    confirmacion = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'Pago_Inscripciones'
