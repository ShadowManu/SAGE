from django.contrib import admin

from estacionamientos.models import Estacionamiento, Reserva, Puesto, Pago

admin.site.register(Estacionamiento)
admin.site.register(Reserva)
admin.site.register(Puesto)
admin.site.register(Pago)