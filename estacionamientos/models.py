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
    capacidad = models.IntegerField(null=True, blank=True)
    tarifa = models.IntegerField(null=True, blank=True)
    horaI = models.TimeField(null=True, blank=True)
    horaF = models.TimeField(null=True, blank=True)
    reservaI = models.TimeField(null=True, blank=True)
    reservaF = models.TimeField(null=True, blank=True)
    
    def __unicode__(self):
        return self.nombre_est