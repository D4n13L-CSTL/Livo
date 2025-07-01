# membresias/models.py
from django.db import models
from clubes.models import Club, ClubAtleta

class MembresiaClub(models.Model):
    PLANES = [
        ('BASICO', 'Básico'),
        ('ESTANDAR', 'Estándar'),
        ('PREMIUM', 'Premium'),
    ]
    
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    plan = models.CharField(max_length=20, choices=PLANES)
    precio_mensual = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_inicio = models.DateField()
    fecha_proximo_pago = models.DateField()
    activa = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.club} - {self.plan}"

class PagoMembresia(models.Model):
    METODOS_PAGO = [
        ('TARJETA', 'Tarjeta de crédito/débito'),
        ('TRANSFERENCIA', 'Transferencia bancaria'),
        ('EFECTIVO', 'Efectivo'),
    ]
    
    membresia = models.ForeignKey(MembresiaClub, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateField()
    metodo_pago = models.CharField(max_length=20, choices=METODOS_PAGO)
    referencia = models.CharField(max_length=100)
    
    def __str__(self):
        return f"Pago de {self.monto} por {self.membresia}"











class PagoMensualidad(models.Model):
    atleta_club = models.ForeignKey(ClubAtleta, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateField()
    mes_correspondiente = models.DateField()
    #metodo_pago = models.CharField(max_length=20, choices=METODOS_PAGO)
    confirmado = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Pago de {self.monto} por {self.atleta_club}"