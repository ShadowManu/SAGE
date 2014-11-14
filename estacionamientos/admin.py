from django.contrib import admin
from estacionamientos.models import Estacionamiento, Reserva, Puesto

admin.site.register(Estacionamiento)
admin.site.register(Reserva)
admin.site.register(Puesto)
