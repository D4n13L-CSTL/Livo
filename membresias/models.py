# membresias/models.py
from django.db import models
from clubes.models import Club

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

class AtletaClub(models.Model):
    atleta = models.ForeignKey('atletas.Atleta', on_delete=models.CASCADE)
    club = models.ForeignKey('clubes.Club', on_delete=models.CASCADE)
    fecha_inscripcion = models.DateField(auto_now_add=True)
    fecha_baja = models.DateField(null=True, blank=True)
    activo = models.BooleanField(default=True)
    cuota_mensual = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        unique_together = ('atleta', 'club')
    
    def __str__(self):
        return f"{self.atleta} en {self.club}"

class PagoMensualidad(models.Model):
    atleta_club = models.ForeignKey(AtletaClub, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateField()
    mes_correspondiente = models.DateField()
    #metodo_pago = models.CharField(max_length=20, choices=METODOS_PAGO)
    confirmado = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Pago de {self.monto} por {self.atleta_club}"