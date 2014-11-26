from django.db import models

class Estacionamiento(models.Model):
    nombre_duenio = models.CharField(max_length=30)
    nombre_est = models.CharField(max_length=30,unique=True)
    direccion = models.CharField(max_length=30)
    telefono1 = models.IntegerField(max_length=11)
    telefono2 = models.IntegerField(max_length=11,null=True, blank=True)
    telefono3 = models.IntegerField(max_length=11,null=True, blank=True)
    email1 = models.EmailField()
    email2 = models.EmailField(null=True, blank=True)
    email3 = models.EmailField(null=True, blank=True)
    rif = models.IntegerField()
    capacidad = models.IntegerField()
    tarifa = models.DecimalField(max_digits=7, decimal_places=2)
    horaI = models.TimeField()
    horaF = models.TimeField()
    reservaI = models.TimeField(null=True, blank=True)
    reservaF = models.TimeField(null=True, blank=True)
    
    def __unicode__(self):
        return self.nombre_est
    
    def  __str__(self):
        return self.nombre_est
        


class Reserva(models.Model):
    estacionamiento = models.ForeignKey(Estacionamiento)
    #puesto = models.ForeignKey(Puesto)
    horaInicio = models.TimeField()
    horaFin = models.TimeField()
    
    def __unicode__(self):
        return "Reserva"
    
    def __str__(self):
        return "Reserva"
    
    
class Pago(models.Model):
    nombre = models.CharField(max_length=30)
    cedula = models.PositiveIntegerField(max_length=8)
    tipoTarjeta = models.CharField(max_length=8)
    numeroTarjeta = models.CharField(max_length=16)
    pago = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)

    def __unicode__(self):
        return "Pago"
    
    def __str__(self):
        return "Pago"
