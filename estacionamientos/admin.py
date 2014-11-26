from django.contrib import admin
from estacionamientos.models import Estacionamiento, Reserva, Pago

admin.site.register(Estacionamiento)
admin.site.register(Reserva)
admin.site.register(Pago)